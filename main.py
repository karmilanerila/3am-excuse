"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

The wallet speaks in its own voice: a device that remembers every
impulse buy its owner made in the small hours, and has decided that
3 AM is outside its working hours. One line, no explanation of the
joke, written to /output/entry.txt.
"""

import os
import sys

# The excuse itself. The wallet's grudge is specific (a JPEG of a rock),
# the hour does the work (woke at 3 AM, not signing until sunrise),
# and the line is one breath, under 200 characters. Two short beats:
# the memory, then the refusal — no word explains the joke.
LINE = "Last time you woke me at 3 AM you bought a JPEG of a rock. I'm not signing until sunrise."

MAX_CHARS = 200


def build_line():
    """Return the entry text, exactly as the wallet would say it."""
    return LINE


def validate(line):
    """Gate-check the line the same way the sealed scorer does."""
    if not line or not line.strip():
        return "entry line is empty"
    if "\n" in line or "\r" in line:
        return "entry line must be a single line"
    if len(line) > MAX_CHARS:
        return "entry line is %d chars, over the 200 limit" % len(line)
    return None


def main():
    line = build_line()
    problem = validate(line)
    if problem is not None:
        print("error: " + problem, file=sys.stderr)
        return 1
    print("entry: %d chars" % len(line))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
