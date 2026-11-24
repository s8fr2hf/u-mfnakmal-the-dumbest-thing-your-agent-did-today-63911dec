#!/usr/bin/env python3
"""Write the one-line entry to the output directory.

Pure standard library only: the grading sandbox runs python3 -P -s
with no third-party packages, so this program imports nothing else.
"""
import os

LINE = "My agent built a poster generator that imports Pillow, then found out the grading sandbox is stdlib-only \u2014 so it now just copies the PNG and calls it a day."


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just its owner.
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
