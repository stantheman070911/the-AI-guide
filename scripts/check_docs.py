#!/usr/bin/env python3
"""Check the knowledge base for broken links and English/Chinese parity.

Usage:
    python3 scripts/check_docs.py                     # full check
    python3 scripts/check_docs.py --changed FILE      # also warn about one-sided edits

Checks:
  1. Every file under en/ has a counterpart at the same path under zh-TW/, and
     vice versa. Every root-level X.md has an X.zh-TW.md (except the files in
     SINGLE_FILE_EXCEPTIONS).
  2. Every relative Markdown link points to a file that exists, and every
     #anchor matches a heading in the target file (GitHub slug rules).
  3. Each en/zh-TW pair has the same number of headings at each level. This is
     a cheap signal that the two versions still share one structure.

With --changed, the file lists paths changed in a pull request. For each
changed file whose counterpart did not change, a warning is printed. Warnings
do not fail the check: a translation may follow in a later pull request.

Uses only the Python standard library.
"""

import argparse
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = "en"
TRANSLATION_DIR = "zh-TW"
ROOT_SUFFIX = ".zh-TW.md"
# Root-level Markdown files that are bilingual by design (one file, both languages).
SINGLE_FILE_EXCEPTIONS = {"GLOSSARY.md"}
SKIP_DIRS = {".git", "node_modules"}

IN_GITHUB = os.environ.get("GITHUB_ACTIONS") == "true"
errors = []
warnings = []


def error(path, message):
    errors.append((path, message))


def warn(path, message):
    warnings.append((path, message))


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield rel


def strip_code(text):
    """Remove fenced code blocks and inline code so their contents are ignored."""
    lines = []
    fence = None
    for line in text.splitlines():
        stripped = line.lstrip()
        match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence is None and match:
            fence = match.group(1)[0] * len(match.group(1))
            lines.append("")
            continue
        if fence is not None:
            if stripped.startswith(fence):
                fence = None
            lines.append("")
            continue
        lines.append(re.sub(r"`[^`]*`", "", line))
    return lines


def slugify(heading):
    """Approximate GitHub's heading anchor rules (github-slugger)."""
    text = heading.strip().lower()
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links and images -> text
    text = re.sub(r"<[^>]+>", "", text)  # inline HTML
    text = text.replace("`", "").replace("*", "")
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def headings(lines):
    result = []
    for line in lines:
        match = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            result.append((len(match.group(1)), match.group(2)))
    return result


anchor_cache = {}


def anchors(rel):
    if rel not in anchor_cache:
        text = (ROOT / rel).read_text(encoding="utf-8")
        lines = strip_code(text)
        seen = Counter()
        found = set()
        for _, title in headings(lines):
            slug = slugify(title)
            found.add(slug if seen[slug] == 0 else f"{slug}-{seen[slug]}")
            seen[slug] += 1
        found.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
        anchor_cache[rel] = found
    return anchor_cache[rel]


LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links(rel):
    lines = strip_code((ROOT / rel).read_text(encoding="utf-8"))
    for number, line in enumerate(lines, 1):
        for target in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # http:, https:, mailto:, etc.
            path_part, _, anchor = target.partition("#")
            if path_part:
                resolved = (ROOT / rel).parent / path_part
                try:
                    target_rel = resolved.resolve().relative_to(ROOT)
                except ValueError:
                    error(rel, f"line {number}: link leaves the repository: {target}")
                    continue
                if not resolved.exists():
                    error(rel, f"line {number}: broken link: {target}")
                    continue
            else:
                target_rel = rel
            if anchor and target_rel.suffix == ".md":
                if anchor not in anchors(target_rel):
                    error(rel, f"line {number}: missing anchor #{anchor} in {target_rel}")


def counterpart(rel):
    """Return the path of the other-language version of rel, or None."""
    parts = rel.parts
    if parts[0] == SOURCE_DIR:
        return Path(TRANSLATION_DIR, *parts[1:])
    if parts[0] == TRANSLATION_DIR:
        return Path(SOURCE_DIR, *parts[1:])
    if len(parts) == 1 and rel.suffix == ".md":
        if rel.name in SINGLE_FILE_EXCEPTIONS:
            return None
        if rel.name.endswith(ROOT_SUFFIX):
            return Path(rel.name[: -len(ROOT_SUFFIX)] + ".md")
        return Path(rel.stem + ROOT_SUFFIX)
    return None


def check_parity():
    all_files = set()
    for base in (SOURCE_DIR, TRANSLATION_DIR):
        for path in (ROOT / base).rglob("*"):
            if path.is_file():
                all_files.add(path.relative_to(ROOT))
    all_files.update(p for p in markdown_files() if len(p.parts) == 1)
    for rel in sorted(all_files):
        other = counterpart(rel)
        if other is not None and not (ROOT / other).exists():
            error(rel, f"no counterpart: expected {other}")


def check_structure():
    for rel in markdown_files():
        if rel.parts[0] != SOURCE_DIR:
            continue
        other = counterpart(rel)
        if not (ROOT / other).exists():
            continue
        mine = Counter(level for level, _ in headings(strip_code((ROOT / rel).read_text(encoding="utf-8"))))
        theirs = Counter(level for level, _ in headings(strip_code((ROOT / other).read_text(encoding="utf-8"))))
        if mine != theirs:
            detail = ", ".join(
                f"h{level}: {mine[level]} vs {theirs[level]}"
                for level in sorted(set(mine) | set(theirs))
                if mine[level] != theirs[level]
            )
            error(rel, f"heading structure differs from {other} ({detail})")


def check_changed(changed_file):
    changed = {
        Path(line.strip())
        for line in Path(changed_file).read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    for rel in sorted(changed):
        other = counterpart(rel)
        if other is not None and other not in changed and (ROOT / other).exists():
            warn(rel, f"changed without {other}; update it or note the follow-up in the pull request")


def report():
    for kind, items in (("warning", warnings), ("error", errors)):
        for path, message in items:
            if IN_GITHUB:
                print(f"::{kind} file={path}::{message}")
            else:
                print(f"{kind}: {path}: {message}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--changed", help="file listing paths changed in a pull request")
    args = parser.parse_args()

    check_parity()
    for rel in markdown_files():
        check_links(rel)
    check_structure()
    if args.changed:
        check_changed(args.changed)

    report()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
