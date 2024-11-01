def dayscnt(tasks: list, k: int) -> int:
    ans = 0
    tasks = sorted(tasks)
    n = len(tasks)
    while n > 0:
        right = 0
        start = tasks[0]
        while right < n:
            if abs(start - tasks[right]) > k:
                start = tasks[right]
                tasks.pop(right)
                n -= 1
            else:
                right += 1
        ans += 1
        tasks.pop(0)
        n -= 1
    return ans


# print(dayscnt([3, 8, 5, 7, 1, 2, 4, 9, 6], 2) == 3)
assert dayscnt([806439, 842684], 100000) == 2
assert dayscnt([115622805], 1) == 1
assert dayscnt([4, 2, 1], 2) == 2
assert dayscnt([3, 8, 5, 7, 1, 2, 4, 9, 6], 2) == 3
assert dayscnt([1, 3, 1], 0) == 2
assert dayscnt([32, 77, 1, 100], 4) == 1


def main():
    n, k = map(int, input().split())
    tasks = list(map(int, input().split()))
    print(dayscnt(tasks, k))


if __name__ == "__main__":
    main()
