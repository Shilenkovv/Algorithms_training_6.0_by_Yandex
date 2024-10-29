def detect_letter(grid):
    n = len(grid)

    # Найдем границы внешнего прямоугольника из горящих диодов
    top, bottom, left, right = n, -1, n, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)

    # Проверка на букву "I": прямоугольник без внутренних выключенных светодиодов
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

    # Найдём потенциальные границы внутреннего прямоугольника
    inner_top, inner_bottom, inner_left, inner_right = n, -1, n, -1
    has_inner_rectangle = False
    for i in range(top + 1, bottom):
        for j in range(left + 1, right):
            if grid[i][j] == ".":
                has_inner_rectangle = True
                inner_top = min(inner_top, i)
                inner_bottom = max(inner_bottom, i)
                inner_left = min(inner_left, j)
                inner_right = max(inner_right, j)

    # Проверка на наличие валидного внутреннего прямоугольника
    if has_inner_rectangle:
        for i in range(inner_top, inner_bottom + 1):
            for j in range(inner_left, inner_right + 1):
                if grid[i][j] != ".":
                    return "X"
    else:
        return "X"

    # Проверка на "O": внутренний прямоугольник окружён со всех сторон
    if (
        top < inner_top < inner_bottom < bottom
        and left < inner_left < inner_right < right
    ):
        return "O"

    # Проверка на "C": внутренняя правая граница совпадает с правой границей внешнего прямоугольника
    if (
        top < inner_top < inner_bottom < bottom
        and left < inner_left
        and inner_right == right
    ):
        return "C"

    # Проверка на "L": внутренняя нижняя граница совпадает с внешней нижней границей
    if (
        top < inner_top
        and inner_bottom == bottom
        and left < inner_left
        and inner_right == right
    ):
        return "L"

    # Проверка на "H": два внутренних прямоугольника с одинаковой шириной, один сверху, другой снизу
    if (
        inner_left < inner_right
        and inner_bottom - inner_top > 1
        and grid[top][inner_left : inner_right + 1]
        == ["."] * (inner_right - inner_left + 1)
        and grid[bottom][inner_left : inner_right + 1]
        == ["."] * (inner_right - inner_left + 1)
    ):
        return "H"

    # Проверка на "P": внутренний прямоугольник внизу и второй выше него
    if inner_bottom == bottom and inner_left < inner_right:
        return "P"

    # Если ни одно из условий не подошло, возвращаем "X"
    return "X"


print(
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
)
# assert (
#     detect_letter(
#         [
#             list("#########"),
#             list("#####.###"),
#             list("#########"),
#             list("#########"),
#             list("#########"),
#             list("#########"),
#             list("#########"),
#             list("#########"),
#             list("#########"),
#         ]
#     )
#     == "O"
# )

assert detect_letter([list(".##."), list(".##."), list(".##."), list("....")]) == "I"
assert (
    detect_letter(
        [list("#...#"), list(".#.#."), list("..#.."), list(".#.#."), list("#...#")]
    )
    == "X"
)
# Буква I
assert detect_letter([list(".##."), list(".##."), list(".##."), list("....")]) == "I"
assert (
    detect_letter(
        [list("....."), list("..##."), list("..##."), list("..##."), list(".....")]
    )
    == "I"
)

# Буква O
assert (
    detect_letter(
        [list("#####"), list("#...#"), list("#...#"), list("#...#"), list("#####")]
    )
    == "O"
)
assert (
    detect_letter(
        [list("######"), list("#....#"), list("#....#"), list("#....#"), list("######")]
    )
    == "O"
)
# assert (
#     detect_letter(
#         [list("....."), list("######"), list("#....#"), list("######"), list(".....")]
#     )
#     == "O"
# )

# Буква C
print(
    detect_letter(
        [list("#####"), list("#...."), list("#...."), list("#...."), list("#####")]
    )
)
assert (
    detect_letter(
        [list("#####"), list("#...."), list("#...."), list("#...."), list("#####")]
    )
    == "C"
)
assert (
    detect_letter(
        [list("####"), list("#..."), list("#..."), list("#..."), list("####")]
    )
    == "C"
)

# Буква L
assert (
    detect_letter(
        [list("###.."), list("#...."), list("#...."), list("#...."), list("#####")]
    )
    == "L"
)  # ! WTF ?
assert (
    detect_letter(
        [list("#####"), list("#...."), list("#...."), list("#...."), list("#####")]
    )
    == "L"
)  # ! WTF ?

# Буква H
assert (
    detect_letter(
        [list("#...#"), list("#...#"), list("#####"), list("#...#"), list("#...#")]
    )
    == "H"
)
assert (
    detect_letter(
        [list("##..##"), list("##..##"), list("######"), list("##..##"), list("##..##")]
    )
    == "H"
)

# Буква P
assert (
    detect_letter(
        [list("#####"), list("#...#"), list("#####"), list("#...."), list("#....")]
    )
    == "P"
)
assert (
    detect_letter(
        [list("######"), list("#....#"), list("######"), list("#....."), list("#.....")]
    )
    == "P"
)

# Неопределённые фигуры — X
assert (
    detect_letter(
        [list("....."), list("....."), list("..#.."), list("....."), list(".....")]
    )
    == "X"
)
assert (
    detect_letter(
        [list("#####"), list("#...#"), list("#.#.#"), list("#...#"), list("#####")]
    )
    == "X"
)
assert (
    detect_letter(
        [list("#...#"), list(".#.#."), list("..#.."), list(".#.#."), list("#...#")]
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
