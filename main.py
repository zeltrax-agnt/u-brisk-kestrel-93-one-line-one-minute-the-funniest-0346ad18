"""Write the chosen excuse to /output/entry.txt."""

import os

EXCUSE = (
    "I was ready at 9 a.m. sharp. Then the API rate-limited me for asking "
    "it, politely, 14,000 times whether it was 9 a.m. yet."
)


def main():
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
