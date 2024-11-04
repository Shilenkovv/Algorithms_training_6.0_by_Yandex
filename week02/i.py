def sort_algos(n, al_in, al_us, mood):
    if n == 1:
        return [1]
    algos = [0] * n
    for i in range(n):
        algos[i] = [i, al_in[i], al_us[i]]
    algos_in = sorted(algos, key=lambda x: (x[1], x[2]), reverse=True)
    algos_us = sorted(algos, key=lambda x: (x[2], x[1]), reverse=True)
    ans = [0] * n
    used = set()
    i = in_pointer = us_pointer = 0
    while i < n and in_pointer < n and us_pointer < n:
        if mood[i] == 0:
            while algos_in[in_pointer][0] in used:
                in_pointer += 1
            ans[i] = algos_in[in_pointer][0]
        elif mood[i] == 1:
            while algos_us[us_pointer][0] in used:
                us_pointer += 1
            ans[i] = algos_us[us_pointer][0]
        used.add(ans[i])
        i += 1

    return list(map(lambda x: x + 1, ans))


assert sort_algos(1, [10], [18], [0]) == [1]
assert sort_algos(1, [10], [18], [0]) == [1]
assert sort_algos(5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 0]) == [
    1,
    5,
    2,
    4,
    3,
]
assert sort_algos(
    6, [3, 10, 6, 2, 10, 1], [3, 5, 10, 7, 5, 9], [0, 0, 1, 1, 0, 1]
) == [2, 5, 3, 6, 1, 4]


def main():
    n = int(input())
    al_in = list(map(int, input().split()))
    al_us = list(map(int, input().split()))
    mood = list(map(int, input().split()))
    print(" ".join(map(str, sort_algos(n, al_in, al_us, mood))))


if __name__ == "__main__":
    main()
