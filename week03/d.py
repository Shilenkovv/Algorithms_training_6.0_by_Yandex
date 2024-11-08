def postfix(calc: list) -> float:
    stack = []
    for elem in calc.split():
        if elem.isdigit():
            stack.append(int(elem))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(eval(f"{a}{elem}{b}"))
    return stack[0]


assert postfix("8 9 + 1 7 - *") == -102


def main():
    print(postfix(input().strip()))


if __name__ == "__main__":
    main()
