"""One Line of Earned Pride -- make.fun entry (program/v1).

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene -- a small
person doing something hard, a long effort finally landing.
"""

import os

LINE = (
    "On the last day of summer, the boy who had fallen off his bike "
    "forty-one times rode past his house without wobbling, and his "
    "mother, watching from the porch, did not call out."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > 240:
        raise SystemExit(
            f"entry line is {len(text)} characters, over the 240 limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    out_path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
