def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum[1:]


assert makeprefixsum([1, 3, 5, 10]) == [1, 4, 9, 19]
assert makeprefixsum([1, 3, 5, -10]) == [1, 4, 9, -1]
assert makeprefixsum([0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 0, 1]
assert makeprefixsum([5]) == [5]
assert makeprefixsum([10, -4, 5, 0, 2]) == [10, 6, 11, 11, 13]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(" ".join(map(str, makeprefixsum(nums))))


if __name__ == "__main__":
    main()
