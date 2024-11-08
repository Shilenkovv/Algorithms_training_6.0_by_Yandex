def calc(exp: str):
    try:
        return eval(exp)
    except Exception:
        return "WRONG"


assert calc("1+(2*2 - 3)") == 2
assert calc("1+a+1") == "WRONG"
assert calc("1 1 + 2") == "WRONG"


def main():
    print(calc(input()))


if __name__ == "__main__":
    main()
