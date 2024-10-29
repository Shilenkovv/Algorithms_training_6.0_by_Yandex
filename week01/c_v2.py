def detect_letter(grid):
    n = len(grid)

    # Найдём границы внешнего прямоугольника из горящих диодов
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

    # Проверка на букву "L": левая полоса с заполненной нижней строкой
    if bottom == n - 1 and right != left:
        is_l = True
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if (i < bottom and j > left and grid[i][j] == "#") or (
                    i == bottom and grid[i][left] != "#"
                ):
                    is_l = False
                    break
            if not is_l:
                break
        if is_l:
            return "L"

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

    # Проверка на "O": внутренний прямоугольник окружён со всех сторон
    if (
        has_inner_rectangle
        and top < inner_top <= inner_bottom < bottom
        and left < inner_left <= inner_right < right
    ):
        is_o = True
        for i in range(inner_top, inner_bottom + 1):
            for j in range(inner_left, inner_right + 1):
                if grid[i][j] != ".":
                    is_o = False
                    break
            if not is_o:
                break
        if is_o:
            return "O"

    # Проверка на "P": наличие внутреннего прямоугольника в верхней части фигуры
    if (
        has_inner_rectangle
        and top < inner_top <= inner_bottom < bottom
        and left < inner_left <= inner_right < right
        and inner_bottom < bottom  # внутренний прямоугольник не закрыт снизу
    ):
        return "P"

    # Проверка на "C": внутренняя правая граница совпадает с правой границей внешнего прямоугольника
    if (
        top < inner_top <= inner_bottom < bottom
        and left < inner_left
        and inner_right == right
    ):
        return "C"

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

    # Если ни одно из условий не подошло, возвращаем "X"
    return "X"


# Тесты
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

assert detect_letter([list(".##."), list(".##."), list(".##."), list("....")]) == "I"
assert (
    detect_letter(
        [list("#...#"), list(".#.#."), list("..#.."), list(".#.#."), list("#...#")]
    )
    == "X"
)

# Буква P
assert (
    detect_letter(
        [list("#####"), list("#...#"), list("#####"), list("#...."), list("#....")]
    )
    == "P"
)

print("All tests passed.")
