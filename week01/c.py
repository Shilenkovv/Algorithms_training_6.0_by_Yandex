def detect_letter(grid):
    n = len(grid)

    # Найдём границы внешнего прямоугольника
    top, bottom, left, right = n, -1, n, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)
    if bottom == -1 and right == -1:
        return "X"

    # 1 Проверка на "I" — сплошной прямоугольник без внутренних пустых областей
    is_i = True
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] == ".":
                is_i = False
                break
        if not is_i:
            break
    if is_i:
        return "I"

    # 2 Определим границы внутреннего прямоугольника
    inner_top, inner_bottom, inner_left, inner_right = n, -1, n, -1
    has_inner_rectangle = False
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] == ".":
                has_inner_rectangle = True
                inner_top = min(inner_top, i)
                inner_bottom = max(inner_bottom, i)
                inner_left = min(inner_left, j)
                inner_right = max(inner_right, j)

    # 3 Проверка на "O" — внутренний прямоугольник окружён со всех сторон
    is_O = (
        has_inner_rectangle
        and top < inner_top <= inner_bottom < bottom
        and left < inner_left <= inner_right < right
    )
    if is_O:
        # Проверяем, что вся внутренняя область заполнена "."
        for i in range(inner_top, inner_bottom + 1):
            for j in range(inner_left, inner_right + 1):
                if grid[i][j] == "#":
                    is_O = False
                    break
            if not is_O:
                break
        if is_O:
            return "O"

    # 4 Проверка на "C"
    if (
        has_inner_rectangle
        and top < inner_top <= inner_bottom < bottom
        and inner_right == right
        and left < inner_left <= right
    ):
        return "C"

    # 5 Проверка на "L"
    is_L = (
        all(
            grid[bottom][j] == "#" for j in range(left, right + 1)
        )  # нижняя строка
        and all(
            grid[i][left] == "#" for i in range(top, bottom + 1)
        )  # левая сторона
        and top == inner_top  # проверка на верхнюю часть
        and inner_right == right
        and all(
            grid[inner_bottom][j] != "#"
            for j in range(inner_left, inner_right + 1)
        )  # целостность нижней части внутреннего прямоугольника
        and all(
            grid[inner_top][j] != "#"
            for j in range(inner_left, inner_right + 1)
        )
    )
    if is_L:
        return "L"

    # 6 Проверка на "H" — два внутренних прямоугольника с одинаковой шириной
    # один сверху, другой снизу
    if (
        has_inner_rectangle
        and inner_left <= inner_right
        and inner_bottom - inner_top > 1
        and grid[top][inner_left : inner_right + 1]
        == ["."] * (inner_right - inner_left + 1)
        and grid[bottom][inner_left : inner_right + 1]
        == ["."] * (inner_right - inner_left + 1)
    ):
        return "H"

    # 7 Проверка на "P" — внутренний прямоугольник внизу и второй выше него
    is_P = True
    for i in range(inner_top, inner_bottom + 1):
        if len(set(grid[i][inner_left:inner_right])) != 1:
            is_P = False
    if is_P:
        if (
            has_inner_rectangle
            and inner_bottom == bottom
            and inner_left < inner_right
            and inner_top != top
            and inner_right == right
        ):
            return "P"

    # Если ни одно из условий не подошло, возвращаем "X"
    return "X"


assert (
    detect_letter(
        [
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
            list(".........."),
        ]
    )
    == "X"
)
assert (
    detect_letter(
        [
            list(".........."),
            list(".#########"),
            list(".##......#"),
            list(".##....#.#"),
            list(".##......#"),
            list(".#########"),
            list(".##......."),
            list(".##......."),
            list(".##......."),
            list(".........."),
        ]
    )
    == "X"
)
assert (
    detect_letter(
        [
            list("##########"),
            list("#........#"),
            list("##########"),
            list("##########"),
            list("##########"),
            list("##########"),
            list("##########"),
            list("#........#"),
            list("#........#"),
            list("#........#"),
        ]
    )
    == "X"
)
assert detect_letter([list("#.#"), list("###"), list("#.#")]) == "H"
assert detect_letter(
    [
        list(".........."),
        list(".####...##"),
        list(".####...##"),
        list(".####...##"),
        list(".####...##"),
        list(".####...##"),
        list(".#########"),
        list(".#########"),
        list(".#########"),
        list(".#########"),
    ]
)
assert (
    detect_letter(
        [
            list(".........."),
            list(".####.####"),
            list(".#########"),
            list(".#########"),
            list(".#......##"),
            list(".#......##"),
            list(".#########"),
            list(".........."),
            list(".........."),
            list(".........."),
        ]
    )
    == "X"
)
assert (
    detect_letter(
        [
            list("#######"),
            list("######."),
            list("#######"),
            list("#######"),
            list("#######"),
            list("#######"),
            list("#######"),
        ]
    )
) == "C"
assert detect_letter([list("#."), list("##")]) == "L"

assert (
    detect_letter(
        [
            list("#########"),
            list("#####.###"),
            list("#########"),
            list("#########"),
            list("#########"),
            list("#########"),
            list("#########"),
            list("#########"),
            list("#########"),
        ]
    )
    == "O"
)

assert (
    detect_letter([list(".##."), list(".##."), list(".##."), list("....")])
    == "I"
)
assert (
    detect_letter(
        [
            list("#...#"),
            list(".#.#."),
            list("..#.."),
            list(".#.#."),
            list("#...#"),
        ]
    )
    == "X"
)
# Буква I
assert (
    detect_letter([list(".##."), list(".##."), list(".##."), list("....")])
    == "I"
)
assert (
    detect_letter(
        [
            list("....."),
            list("..##."),
            list("..##."),
            list("..##."),
            list("....."),
        ]
    )
    == "I"
)

# Буква O
assert (
    detect_letter(
        [
            list("#####"),
            list("#...#"),
            list("#...#"),
            list("#...#"),
            list("#####"),
        ]
    )
    == "O"
)
assert (
    detect_letter(
        [
            list("######"),
            list("#....#"),
            list("#....#"),
            list("#....#"),
            list("#....#"),
            list("######"),
        ]
    )
    == "O"
)

# Буква C
assert (
    detect_letter(
        [
            list("#####"),
            list("#...."),
            list("#...."),
            list("#...."),
            list("#####"),
        ]
    )
    == "C"
)
assert (
    detect_letter([list("####"), list("#..."), list("#..."), list("####")])
    == "C"
)

assert (
    detect_letter(
        [
            list("#...."),
            list("#...."),
            list("#...."),
            list("#...."),
            list("#####"),
        ]
    )
    == "L"
)

# Буква H
assert (
    detect_letter(
        [
            list("#...#"),
            list("#...#"),
            list("#####"),
            list("#...#"),
            list("#...#"),
        ]
    )
    == "H"
)
assert (
    detect_letter(
        [
            list("##..##"),
            list("##..##"),
            list("######"),
            list("##..##"),
            list("##..##"),
        ]
    )
    == "H"
)

# Буква P
assert (
    detect_letter(
        [
            list("#####"),
            list("#...#"),
            list("#####"),
            list("#...."),
            list("#...."),
        ]
    )
    == "P"
)

# Неопределённые фигуры — X
assert (
    detect_letter(
        [
            list("....."),
            list("....."),
            list("..#.."),
            list("....."),
            list("....."),
        ]
    )
    == "I"
)
assert (
    detect_letter(
        [
            list("#####"),
            list("#...#"),
            list("#.#.#"),
            list("#...#"),
            list("#####"),
        ]
    )
    == "X"
)
assert (
    detect_letter(
        [
            list("#...#"),
            list(".#.#."),
            list("..#.."),
            list(".#.#."),
            list("#...#"),
        ]
    )
    == "X"
)
assert (
    detect_letter(
        [
            list(".........."),
            list(".........."),
            list("..###....."),
            list("..###....."),
            list("..###....."),
            list("..###....."),
            list("..###.####"),
            list("..########"),
            list("..########"),
            list(".........."),
        ]
    )
    == "X"
)


def main():
    board = []

    n = int(input())
    for i in range(n):
        row = list(input())
        board.append(row)

    # Вывод результата
    letter = detect_letter(board)
    print(letter)


if __name__ == "__main__":
    main()
