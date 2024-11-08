def window_min(n: int, k: int, nums: list) -> list:
    deck = []
    ans = []
    for i, elem in enumerate(nums):
        while deck and deck[-1] > elem:
            deck.pop()
        deck.append(elem)
        if i >= k - 1:
            ans.append(deck[0])
            if nums[i - k + 1] == deck[0]:
                deck.pop(0)
    return ans


assert window_min(7, 3, [1, 3, 2, 4, 5, 3, 1]) == [1, 2, 2, 3, 1]
assert window_min(7, 2, [1, 5, 8, 14, 1, 19, 16]) == [1, 5, 8, 1, 1, 16]
assert window_min(7, 1, [1, 5, 8, 14, 1, 19, 16]) == [1, 5, 8, 14, 1, 19, 16]
assert window_min(2, 2, [1, 3]) == [1]
assert window_min(2, 2, [3, 1]) == [1]
assert window_min(1, 1, [10]) == [10]
assert window_min(5, 2, [1, 1, 1, 1, 1]) == [1, 1, 1, 1]


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    # window_min(n, k, nums)
    print(*window_min(n, k, nums), sep="\n")


if __name__ == "__main__":
    main()
