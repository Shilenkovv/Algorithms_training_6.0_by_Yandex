def brackets(seq: str) -> str:
    deck = []
    d = {"(": ")", "[": "]", "{": "}"}
    for c in seq:
        if c in d:
            deck.append(c)
        else:
            if deck:
                if c == d.get(deck[-1]):
                    deck.pop()
                    continue
            return "no"
    if deck:
        return "no"
    return "yes"


assert brackets("()[]") == "yes"
assert brackets("([)]") == "no"
assert brackets("(") == "no"
assert brackets("(([[[]]]))") == "yes"
assert brackets("(([[[]])])") == "no"
assert brackets("()(") == "no"
assert brackets("())") == "no"
assert brackets(")(") == "no"


def main() -> None:
    seq = input()
    print(brackets(seq))


if __name__ == "__main__":
    main()
