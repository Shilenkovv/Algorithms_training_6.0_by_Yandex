def max_mul(lst):
    max_mul = -10e10
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            curr_mul = lst[i] * lst[j]
            if curr_mul > max_mul:
                a, b = lst[i], lst[j]
                max_mul = curr_mul
    if a <= b:
        return a, b
    return b, a


with open(
    "week01/e.txt",
    "r",
) as f:
    n = int(f.readline())
    for i in range(n):
        tst = f.readline().strip()
        print(f"test {tst}")
        tst = tst.split()
        tst = [int(x) for x in tst[1:]]
        a, b = max_mul(tst)
        print(a, b)
