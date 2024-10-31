def prefixsum_auto(nums, k):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

    left = ans = cur_sum = 0
    right = 1
    while right < len(prefixsum):
        cur_sum = prefixsum[right] - prefixsum[left]
        if cur_sum <= k:
            if prefixsum[right] - prefixsum[left] == k:
                ans += 1
            right += 1
        else:
            while left < right and cur_sum > k:
                left += 1
                cur_sum = prefixsum[right] - prefixsum[left]
    return ans


assert prefixsum_auto([17, 7, 10, 7, 10], 17) == 4
assert prefixsum_auto([1, 2, 3, 4, 1], 10) == 2
assert prefixsum_auto([3, 3, 3], 10) == 0
assert prefixsum_auto([1], 1) == 1
assert prefixsum_auto([2], 1) == 0
assert prefixsum_auto([3, 2, 50, 100, 3, 1, 1, 5], 5) == 3


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(prefixsum_auto(nums, k))


if __name__ == "__main__":
    main()
