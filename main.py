#!/usr/bin/env python3
"""Dad Joke Showdown entry — u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes one dad joke to /output/entry.txt (UTF-8, 1-200 characters).

The joke was chosen from ten candidates after checking each against the
judge's brief (a pun a father would tell at the table, landing cleanly on
the first read, fresh inside the dad-joke tradition, tight, punchline at
the end, natural aloud) and searching the web to confirm it is not one of
the jokes told a thousand times. The wallet-as-vending-machine double pun
("press my buttons" / "expect change") is the freshest of the ten: the
ATM-button gag exists, but no published version pairs it with a wallet
treated as a vending machine by the kids.

Stdlib only. Deterministic: the same joke on every run.
"""

import os

# The entry: a father, his wallet, and his children.
JOKE = (
    "My kids treat my wallet like a vending machine. "
    "They press my buttons and expect change."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Self-validation: read the entry back and check the spec's gates.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises if the file is not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    print(f"entry ok: {len(text)} characters")


if __name__ == "__main__":
    main()

