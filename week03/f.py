def min_cbs(n: int, w: str, s: str) -> str:
    stack = []
    d_o = {"(": ")", "[": "]"}
    d_c = {")": "(", "]": "["}
    for elem in s:
        if elem in d_o:
            stack.append(elem)
        else:
            if stack and d_c.get(elem) == stack[-1]:
                stack.pop()

    while len(s) < n:
        while n - len(s) - len(stack) >= 2:
            for elem in w:
                if elem in d_o:
                    s += elem
                    stack.append(elem)
                    break
                else:
                    if stack and d_o.get(stack[-1]) == elem:
                        s += elem
                        stack.pop()
                        break
        s += d_o.get(stack[-1])
        stack.pop()
    return s


assert min_cbs(10, "][()", "([](") == "([]([][]))"
assert min_cbs(6, "])([", "") == "()()()"
assert min_cbs(6, "()[]", "([(") == "([()])"
assert min_cbs(8, "()[]", "([(") == "([(())])"
assert min_cbs(6, "][)(", "([") == "([][])"
assert min_cbs(4, "(][)", "()[]") == "()[]"


def main():
    n = int(input())
    w, s = input(), input()
    print(min_cbs(n, w, s))


if __name__ == "__main__":
    main()
