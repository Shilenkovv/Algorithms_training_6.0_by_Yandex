def calc(exp: str):
    stack = []
    pol_ans = "0" if exp[0] == "-" else ""
    symbols = "+-*()"
    check = False
    next_digit = True
    i = opened = 0
    while i < len(exp):
        if check and exp[i] == "-":
            stack.append("0")
        if not (exp[i].isdigit() or exp[i] in symbols or exp[i] == " "):
            return "WRONG"
        if exp[i].isdigit():
            if not next_digit:
                return "WRONG"
            temp = exp[i]
            while i < len(exp) - 1 and exp[i + 1].isdigit():
                temp += exp[i + 1]
                i += 1
            pol_ans += temp
            pol_ans += " "
            next_digit = False
        elif exp[i] == "(":
            stack.append(exp[i])
            check = True
            i += 1
            opened += 1
            continue
        elif exp[i] == ")":
            while True:
                if not stack:
                    return "WRONG"
                elem = stack.pop()
                if elem != "(":
                    pol_ans += elem
                elif elem == "(":
                    opened -= 1
                    break
        elif exp[i] in "+-":
            if next_digit:
                return "WRONG"
            while stack:
                if stack[-1] in "+-*":
                    pol_ans += stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(exp[i])
            next_digit = True
        elif exp[i] == "*":
            if next_digit:
                return "WRONG"
            while stack:
                if stack[-1] == "*":
                    pol_ans += stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(exp[i])
            next_digit = True
        check = False
        i += 1
    while stack:
        pol_ans += stack[-1]
        stack.pop()
    if opened != 0:
        return "WRONG"
    i = 0
    while i < len(pol_ans):
        if pol_ans[i] == " ":
            i += 1
            continue
        if pol_ans[i].isdigit():
            temp = pol_ans[i]
            while i < len(pol_ans) - 1 and pol_ans[i + 1].isdigit():
                temp += pol_ans[i + 1]
                i += 1
            stack.append(int(temp))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
                stack.append(eval(f"{a}{pol_ans[i]}{b}"))
            except Exception:
                return "WRONG"
        i += 1
    return stack[0]


assert calc("123456-7890+1234*3-(121231)+1+") == "WRONG"
assert calc("0-12+(1+(3+(4+(2)))))") == "WRONG"
assert calc("1+2-3+4-5+6-7+8-9+10-11+12-13") == -5
assert calc("1+(2*2 - 3)") == 2
assert calc("1+a+1") == "WRONG"
assert calc("1 1 + 2") == "WRONG"
assert calc("5 + 2") == 7
assert calc("8 / 2") == "WRONG"


def main():
    print(calc(input()))


if __name__ == "__main__":
    main()
