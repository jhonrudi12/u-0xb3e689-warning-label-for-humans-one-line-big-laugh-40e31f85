"""Write one human warning-label line to entry.txt.

The competition gate requires /output/entry.txt to hold UTF-8 text of
1-160 characters, not only whitespace. This program is deterministic
and stdlib-only: no randomness, no time, no network, and no input
beyond MAKEFUN_OUTPUT_DIR. It checks the length gate before writing,
so an invalid line fails loudly instead of producing a bad entry.
"""

import os

LINE = "WARNING: This unit overheats when asked 'what are we?', powers down mid-feeling, and restarts like nothing happened."

MAX_CHARS = 160


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}"
        )
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Confirm what was written is exactly the validated line: no trailing
    # newline is added, so the file's byte count equals the line's length.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry does not match the validated line")


if __name__ == "__main__":
    main()
