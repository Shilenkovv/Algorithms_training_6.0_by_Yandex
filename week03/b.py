def movement(n: int, costs: list) -> list:
    stack = []
    ans = [-1] * n
    for i, elem in enumerate(costs):
        if not stack:
            stack.append((i, elem))
        else:
            while stack and elem < stack[-1][1]:
                ans[stack[-1][0]] = i
                stack.pop()
            stack.append((i, elem))
    return ans


ans_1 = [-1, 4, 3, 4, -1, 6, 9, 8, 9, -1]
assert movement(10, [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]) == ans_1

ans_2 = [1, 3, 3, 4, -1, 7, 7, 8, -1, -1]
assert movement(10, [65, 51, 79, 36, 2, 47, 92, 30, 25, 94]) == ans_2


def main():
    n = int(input())
    costs = list(map(int, input().split()))
    print(" ".join(map(str, movement(n, costs))))


if __name__ == "__main__":
    main()
