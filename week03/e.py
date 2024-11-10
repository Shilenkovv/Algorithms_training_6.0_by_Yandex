def calc(exp: str):
    symbols = "+-*()"
    for sym in exp:
        if not (sym.isdigit() or sym in symbols or sym == " "):
            return "WRONG"
    try:
        return eval(exp)
    except Exception:
        return "WRONG"


# assert calc("1+(2*2 - 3)") == 2
# assert calc("1+a+1") == "WRONG"
# assert calc("1 1 + 2") == "WRONG"
# assert calc("5 + 2") == 7
assert calc("8 / 2") == "WRONG"


def main():
    print(calc(input()))


if __name__ == "__main__":
    main()
