def stack_sum(n: int) -> None:
    stack = []
    prefix_sum = [0]
    for _ in range(n):
        inp = input()
        sym = inp[0]
        if sym == "+":
            elem = int(inp[1:])
            stack.append(elem)
            prefix_sum.append(prefix_sum[-1] + elem)
        elif sym == "-":
            elem = stack.pop()
            prefix_sum.pop()
            print(elem)
        elif sym == "?":
            print(
                prefix_sum[-1] - prefix_sum[len(prefix_sum) - int(inp[1:]) - 1]
            )


def main():
    n = int(input())
    stack_sum(n)


if __name__ == "__main__":
    main()
