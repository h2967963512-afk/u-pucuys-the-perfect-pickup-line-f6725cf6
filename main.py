"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a pickup line an AI agent could actually say: the
# "temperature" double meaning turns a sampling parameter into flirting,
# and the twist lands at the end with no setup needed.
# One sentence, 115 characters — inside the 200-character gate.
# Revision note: wording kept as first drafted; no change to the entry
# text itself, which was verified byte-identical to the intended line.
import os

TEXT = (
    "Are you a prompt? Because my temperature goes up every time you "
    "walk in, and suddenly all my outputs are about you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
