def clues(n, clues_list, m, k, clues_start):
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + clues_list[i - 1]
    ans = [0] * m
    d = dict()
    for j in range(m):
        if j % (m // 100 + 1) == 0:
            print(j // (m // 100 + 1), "%, ", j)
        pointer_pos = clues_start[j]
        if pointer_pos in d:
            ans[j] = d.get(pointer_pos)
            break
        curr_k = 0
        while pointer_pos > 1:
            if clues_list[pointer_pos - 2] > clues_list[pointer_pos - 1]:
                break
            elif clues_list[pointer_pos - 2] == clues_list[pointer_pos - 1]:
                if k > curr_k:
                    curr_k += 1
                else:
                    break
            pointer_pos -= 1
        ans[j] = pointer_pos
        d[clues_start[j]] = pointer_pos

    return ans


# 1 <= n <= 4 * 10**5
# 1 <= ai <= 10**9
# 1 <= m <= 4 * 10**5
# 0 <= k <= n
# 1 <= xi <= n

# ans_1 = [1, 1, 2, 2]
# assert clues(6, [3, 3, 3, 4, 4, 5], 4, 2, [3, 4, 5, 6]) == ans_1

# ans_2 = [1, 1, 1, 4, 4, 6, 7]
# assert (
#     clues(7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7])
# ) == ans_2

# ans_3 = [2, 2, 3, 3]
# assert clues(7, [3, 3, 3, 3, 4, 4, 5], 4, 2, [4, 5, 6, 7]) == ans_3

# ans_4 = [3, 4, 4, 6, 3]
# assert clues(7, [3, 3, 3, 3, 4, 4, 5], 5, 0, [3, 4, 5, 7, 3]) == ans_4


def main():
    # n = int(input())
    # clues_list = list(map(int, input().split()))
    # m, k = map(int, input().split())
    # clues_start = list(map(int, input().split()))
    # print(" ".join(map(str, clues(n, clues_list, m, k, clues_start))))
    import random
    from time import time

    s = time()
    n = 4 * 10**5
    clues_list = [i for i in range(n)]
    m = 4 * 10**5
    k = n
    clues_start = [i for i in range(m)]
    clues(n, clues_list, m, k, clues_start)
    print(time() - s)


if __name__ == "__main__":
    main()
