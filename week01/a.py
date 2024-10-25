def raft(x1: int, y1: int, x2: int, y2: int, x: int, y: int) -> str:
    if x > x2:
        if y > y2:
            return "NE"
        elif y > y1:
            return "E"
        return "SE"
    elif x > x1:
        if y > y2:
            return "N"
        return "S"
    if y > y2:
        return "NW"
    elif y > y1:
        return "W"
    return "SW"


assert raft(-1, -2, 5, 3, 6, 4) == "NE"
assert raft(-1, -2, 5, 3, 6, -3) == "SE"
assert raft(-1, -2, 5, 3, 6, 0) == "E"
assert raft(-1, -2, 5, 3, 0, 5) == "N"
assert raft(-1, -2, 5, 3, 0, -3) == "S"
assert raft(-1, -2, 5, 3, -2, -3) == "SW"
assert raft(-1, -2, 5, 3, -2, 0) == "W"
assert raft(-1, -2, 5, 3, -4, 6) == "NW"


def main() -> None:
    x1, y1, x2, y2, x, y = [int(input()) for _ in range(6)]
    print(raft(x1, y1, x2, y2, x, y))


if __name__ == "__main__":
    main()
