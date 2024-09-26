import random
from typing import Iterable

def practice(words: Iterable[str]) -> None:
    print("Copy the following:")
    ans = " ".join(words)
    correct = None
    while not correct:
        if correct is not None:
            print("\nNot quite, try again:")
        print(ans)
        correct = input() == ans
    print("Great job!")

def main():
    with open("google-10000-english-usa-no-swears.txt") as f:
        words = [w.strip() for w in f.readlines()]

    row_reference = {
        "home": set("oheaidrtns"),
        "top": set("qfuyzxkcwb"),
        "bottom": set(",m.j;glpv"),
    }
    rows = {}

    for row_name in row_reference:
        # 50 most common words that can be typed with this row
        rows[row_name] = []
        for word in words:
            if len(rows[row_name]) >= 50:
                break
            if set(word) <= row_reference[row_name]:
                rows[row_name].append(word)

    for row_name in row_reference:
        random.shuffle(rows[row_name])
        while len(rows[row_name]) >= 10:
            practice(rows[row_name].pop() for _ in range(10))

if __name__ == "__main__":
    main()
