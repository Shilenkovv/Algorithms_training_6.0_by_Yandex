def clothes(tb: int, tr: int, sb: int, sr: int):
    min_t = min(tb, tr)
    min_s = min(sb, sr)
    if min_t == 0:
        return [1, sb + 1 if tb == min_t else sr + 1]
    elif min_s == 0:
        return [tb + 1 if sb == min_s else tr + 1, 1]

    ans = min(
        [min_t + 1, sb + 1 if tb == min_t else sr + 1],
        [tb + 1 if sb == min_s else tr + 1, min_s + 1],
        [1, max(sb, sr) + 1],
        [max(tb, tr) + 1, 1],
        key=lambda x: sum(x),
    )

    return ans


assert clothes(10, 10, 10, 10) == [1, 11]
assert clothes(1, 1, 1, 1) == [1, 2]
assert clothes(6, 2, 7, 3) == [3, 4]
assert clothes(5, 10, 2, 20) == [6, 3]
assert clothes(5, 10, 20, 2) == [11, 1]
assert clothes(10, 5, 20, 2) == [6, 3]
assert clothes(10, 5, 2, 20) == [11, 1]
assert clothes(10, 0, 15, 0) == [1, 1]
assert clothes(10, 0, 2, 20) == [1, 21]
assert clothes(10, 0, 20, 2) == [1, 3]
assert clothes(10, 5, 0, 2) == [11, 1]
assert clothes(10, 5, 20, 0) == [6, 1]


def main():
    tb, tr, sb, sr = [int(input()) for _ in range(4)]
    print(" ".join(map(str, clothes(tb, tr, sb, sr))))


if __name__ == "__main__":
    main()
