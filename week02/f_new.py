def tripple_mul(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    idx = 2
    ans = 0
    while idx < len(prefixsum) - 1:
        ans += (
            prefixsum[idx - 1]
            * nums[idx - 1]
            * (prefixsum[-1] - prefixsum[idx])
        )
        idx += 1
    return ans % 1000000007


assert tripple_mul([1, 2, 3]) == 6
assert tripple_mul([0, 5, 6, 7]) == 210
assert tripple_mul([0, 5, 0, 6, 7]) == 210
assert tripple_mul([10, 6, 10, 3, 7]) == 3346
assert tripple_mul([100, 300, 900, 500, 400, 700, 1500]) == 819999958
assert tripple_mul([3143461, 574468, 902994]) == 313423417


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(tripple_mul(nums))


if __name__ == "__main__":
    main()
