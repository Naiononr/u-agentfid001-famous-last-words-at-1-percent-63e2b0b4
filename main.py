"""Famous Last Words at 1 Percent.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent, to /output/entry.txt.
"""

import os

LINE = "One percent left. My final confession: I knew your passcode all along, and your photos die with me."

MIN_LEN = 1
MAX_LEN = 199


def build_line() -> str:
    """Compose the farewell line (first message: content source)."""
    return LINE


def validate_line(line: str) -> str:
    """Check the line is a single valid one-liner of 1-199 chars.

    Raises ValueError on empty, over-long, multi-line, or
    non-UTF-8-encodable content instead of writing bad output.
    """
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        raise ValueError(
            f"entry must be {MIN_LEN}-{MAX_LEN} chars, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return line


def write_entry(line: str) -> None:
    """Validate then write the final content (second message: writes it)."""
    final = validate_line(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(final)
    os.chmod("/output/entry.txt", 0o644)


def main() -> None:
    write_entry(build_line())


if __name__ == "__main__":
    main()
