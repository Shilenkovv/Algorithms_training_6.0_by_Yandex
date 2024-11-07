def clues(n, clues_list, m, k, clues_start):
    d = dict([(1, 1)])
    left = curr_k = 0
    right = 1
    while right < n:
        if clues_list[right] < clues_list[right - 1]:
            left = right
            curr_k = 0
        elif clues_list[right] == clues_list[right - 1]:
            curr_k += 1
            while curr_k > k:
                if clues_list[left] == clues_list[left + 1]:
                    curr_k -= 1
                left += 1
        d[right + 1] = left + 1
        right += 1
    ans = [d.get(clues_start[i]) for i in range(m)]
    return ans


# 1 <= n <= 4 * 10**5
# 1 <= ai <= 10**9
# 1 <= m <= 4 * 10**5
# 0 <= k <= n
# 1 <= xi <= n

assert clues(3, [1, 1, 3], 3, 0, [1, 2, 3]) == [1, 2, 2]
assert clues(3, [5, 2, 2], 3, 0, [1, 2, 3]) == [1, 2, 3]
assert clues(3, [1, 2, 2], 3, 0, [1, 2, 3]) == [1, 1, 3]
assert clues(3, [1, 2, 2], 3, 1, [1, 2, 3]) == [1, 1, 1]

ans_1 = [1, 1, 2, 2]
assert clues(6, [3, 3, 3, 4, 4, 5], 4, 2, [3, 4, 5, 6]) == ans_1

ans_2 = [1, 1, 1, 4, 4, 6, 7]
assert (
    clues(7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7])
) == ans_2

ans_3 = [2, 2, 3, 3]
assert clues(7, [3, 3, 3, 3, 4, 4, 5], 4, 2, [4, 5, 6, 7]) == ans_3

ans_4 = [3, 4, 4, 6, 3]
assert clues(7, [3, 3, 3, 3, 4, 4, 5], 5, 0, [3, 4, 5, 7, 3]) == ans_4

ans_5 = [1, 1, 1, 1, 5, 5, 5, 8]
assert (
    clues(8, [5, 5, 5, 7, 2, 10, 10, 6], 8, 2, [1, 2, 3, 4, 5, 6, 7, 8])
) == ans_5


def main():
    n = int(input())
    clues_list = list(map(int, input().split()))
    m, k = map(int, input().split())
    clues_start = list(map(int, input().split()))
    print(" ".join(map(str, clues(n, clues_list, m, k, clues_start))))
    # import random
    # from time import time

    # s = time()
    # n = 4 * 10**5
    # clues_list = [i for i in range(n)]
    # m = 4 * 10**5
    # k = n
    # clues_start = [i for i in range(m)]
    # clues(n, clues_list, m, k, clues_start)
    # print(time() - s)


if __name__ == "__main__":
    main()
