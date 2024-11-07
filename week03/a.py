def brackets(seq: str) -> str:
    stack = []
    d = {"(": ")", "[": "]", "{": "}"}
    for c in seq:
        if c in d:
            stack.append(c)
        else:
            if stack:
                if c == d.get(stack[-1]):
                    stack.pop()
                    continue
            return "no"
    if stack:
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
