def vasya(n: int, h: int, chears_height: list, chears_width: list) -> int:
    if n == 1 or sorted(chears_width)[-1] >= h:
        return 0
    chears_width = [x for _, x in sorted(zip(chears_height, chears_width))]
    chears_height.sort()
    delta = [0] * n
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < n:
            delta[i] = chears_height[i] - chears_height[i - 1]
        prefixsum[i] = chears_width[i - 1] + prefixsum[i - 1]
    left = 0
    best_result = float("inf")
    right = 1
    deck = []
    while left < right and right <= n:
        # cur_width = prefixsum[right] - prefixsum[left]  # ! debug
        while deck and deck[-1] < delta[right - 1]:
            deck.pop()
        deck.append(delta[right - 1])
        while prefixsum[right] - prefixsum[left] >= h:
            if right - left == 1:
                return 0
            elif deck[0] <= best_result:
                best_result = deck[0]
            left += 1
            # cur_width = prefixsum[right] - prefixsum[left]  # ! debug
            if deck and deck[0] == delta[left]:
                deck.pop(0)
        # cur_width = prefixsum[right] - prefixsum[left]  # ! debug
        right += 1
    return best_result


assert (
    vasya(
        10,
        10,
        [3, 1, 5, 7, 11, 9, 9, 9, 4, 3],
        [5, 2, 6, 8, 5, 3, 1, 2, 14, 3],
    )
    == 0
)
assert vasya(4, 7, [1, 4, 1, 2], [1, 4, 2, 3]) == 2
assert vasya(5, 6, [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]) == 1

asserts = False


def main():
    if asserts:
        with open("../week03/J_tests.txt", "r") as f:
            for _ in range(17):
                n, h = map(int, f.readline().strip().split())
                chears_height = list(map(int, f.readline().strip().split()))
                chears_width = list(map(int, f.readline().strip().split()))
                assert vasya(n, h, chears_height, chears_width) == int(
                    f.readline()
                )
                f.readline()
        # stress test
        n = 2 * 10**5
        h = 10**9
        chears_height = [x for x in range(n)]
        chears_width = [x for x in range(n)]
    else:
        n, h = map(int, input().split())
        chears_height = list(map(int, input().split()))
        chears_width = list(map(int, input().split()))
        print(vasya(n, h, chears_height, chears_width))


if __name__ == "__main__":
    main()
