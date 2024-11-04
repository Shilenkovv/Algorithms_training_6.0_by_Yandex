def ospace(nums, n):
    # 1 <= n <= 2 * 10 ** 5
    # 1 <= ai <= 10 ** 9

    d_l = {}
    d_r = {}
    prefixsum = [0] * (n + 1)
    prefixsum_rev = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
        prefixsum_rev[n - i] = prefixsum_rev[n + 1 - i] + nums[n - i]
        d_l[i - 1] = d_l.get(i - 2, 0) + prefixsum[i - 1]
        d_r[n - i] = d_r.get(n + 1 - i, 0) + prefixsum_rev[n + 1 - i]
    best_dist = d_l[0] + d_r[0]
    for i in range(1, n):
        cur_dist = d_l[i] + d_r[i]
        if cur_dist < best_dist:
            best_dist = cur_dist
    return best_dist


assert ospace([100, 16, 90], 3) == 190
assert ospace([100], 1) == 0
assert ospace([5, 2, 3, 1], 4) == 10
assert ospace([5, 4, 3, 2, 1], 5) == 15
assert ospace([2, 2, 2, 2, 2], 5) == 12
# import random

# cnt = 2 * 10 ** 5
# assert ospace([random.randint(1, 10**9) for _ in range(cnt)], cnt)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(ospace(nums, n))
    # pass


if __name__ == "__main__":
    main()
