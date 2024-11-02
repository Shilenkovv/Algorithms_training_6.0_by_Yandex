def del_medians(nums):
    nums = sorted(nums)
    ans = [0] * len(nums)
    odd = True if len(nums) % 2 else False
    i = 0
    while len(nums) > 1:
        idx = len(nums) // 2
        if not odd:
            idx -= 1
        ans[i] = nums[idx]
        nums.pop(idx)
        i += 1
        odd = not odd
    ans[-1] = nums[0]
    return ans


assert del_medians([19, 3, 8]) == [8, 3, 19]
assert del_medians([1, 2, 4, 2]) == [2, 2, 1, 4]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(" ".join(map(str, del_medians(nums))))


if __name__ == "__main__":
    main()
