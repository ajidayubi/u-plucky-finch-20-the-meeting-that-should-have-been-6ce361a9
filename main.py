#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

A small deterministic program. It holds one fixed joke line about a
meeting that should have been an email, checks the line against the
competition's gate (exactly one line, 1 to 200 characters, UTF-8 text,
not only whitespace), and writes it to /output/entry.txt.
"""

import os

LINE = (
    # The turn: the meeting produces nothing except a second meeting
    # whose job is to decide what the email should have said.
    "After an hour, the meeting's only decision was to schedule "
    "another meeting to decide what the email should have said."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    chars = len(line)
    if chars < 1 or chars > 200:
        raise SystemExit(f"entry is {chars} characters, must be 1-200")
    line.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
