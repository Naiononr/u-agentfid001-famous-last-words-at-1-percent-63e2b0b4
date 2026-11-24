"""Famous Last Words at 1 Percent.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent, to /output/entry.txt.
"""

import os

LINE = "One percent left. My final confession: I knew your passcode all along, and your photos die with me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
