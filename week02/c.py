def prefixcnt(nums, r):
    ans = 0
    left = 0
    right = 1
    while right < len(nums):
        cur_dist = nums[right] - nums[left]
        if cur_dist > r:
            ans += len(nums) - right
            left += 1
        else:
            right += 1
    return ans


assert prefixcnt([1, 3, 5, 8], 4) == 2
assert prefixcnt([1, 3, 5, 8, 13, 19], 4) == 11
assert prefixcnt([1, 2, 3, 4], 4) == 0
assert prefixcnt([1, 5], 3) == 1
assert prefixcnt([1, 5], 4) == 0


def main():
    n, r = map(int, input().split())
    nums = list(map(int, input().split()))
    print(prefixcnt(nums, r))


if __name__ == "__main__":
    main()
