def rovers(n: int, d: dict, direction_load_d: dict, a: int, b: int) -> None:
    ans = [0] * (n + 1)
    timing = 1
    passed = 0
    fp, sp = min(a, b), max(a, b)
    tp = min(filter(lambda x: x not in [a, b], [1, 2, 3, 4]))
    lp = max(filter(lambda x: x not in [a, b], [1, 2, 3, 4]))
    straight_line = False
    if max(a, b) - min(a, b) == 2:
        straight_line = True
    elif min(a, b) == 1 and max(a, b) == 4:
        fp, sp = sp, fp
    elif min(tp, lp) == 1 and max(tp, lp) == 4:
        tp, lp = lp, tp
    priorities = [fp, sp, tp, lp]
    while passed < n:
        if direction_load_d[fp] > 0 and d[fp][0] != 0:
            ans[d.get(fp)[0]] = timing
            d.get(fp).pop(0)
            direction_load_d[fp] -= 1
            passed += 1
            if direction_load_d[sp] > 0 and d[sp][0] != 0 and straight_line:
                ans[d.get(sp)[0]] = timing
                d.get(sp).pop(0)
                direction_load_d[sp] -= 1
                passed += 1
            elif direction_load_d[sp] > 0:
                if d[sp][0] == 0:
                    d.get(sp).pop(0)
                elif (
                    direction_load_d[sp] > 1
                    and len(d.get(sp)) > direction_load_d[sp]
                ):
                    j = 1
                    while d.get(sp)[j] != 0:
                        j += 1
                    d.get(sp).pop(j)
            if direction_load_d[tp] > 0:
                if d[tp][0] == 0:
                    d.get(tp).pop(0)
                elif (
                    direction_load_d[tp] > 1
                    and len(d.get(tp)) > direction_load_d[tp]
                ):
                    j = 1
                    while d.get(tp)[j] != 0:
                        j += 1
                    d.get(tp).pop(j)
            if direction_load_d[lp] > 0:
                if d[lp][0] == 0:
                    d.get(lp).pop(0)
                elif (
                    direction_load_d[lp] > 1
                    and len(d.get(lp)) > direction_load_d[lp]
                ):
                    j = 1
                    while d.get(lp)[j] != 0:
                        j += 1
                    d.get(lp).pop(j)
            timing += 1
        elif direction_load_d[sp] > 0 and d[sp][0] != 0:
            ans[d.get(sp)[0]] = timing
            passed += 1
            timing += 1
            for priority in priorities[:2]:
                if direction_load_d[priority] > 0:
                    d.get(priority).pop(0)
            direction_load_d[sp] -= 1
            if direction_load_d[tp] > 0:
                if d[tp][0] == 0:
                    d.get(tp).pop(0)
                elif (
                    direction_load_d[tp] > 1
                    and len(d.get(tp)) > direction_load_d[tp]
                ):
                    j = 1
                    while d.get(tp)[j] != 0:
                        j += 1
                    d.get(tp).pop(j)
            if direction_load_d[lp] > 0:
                if d[lp][0] == 0:
                    d.get(lp).pop(0)
                elif (
                    direction_load_d[lp] > 1
                    and len(d.get(lp)) > direction_load_d[lp]
                ):
                    j = 1
                    while d.get(lp)[j] != 0:
                        j += 1
                    d.get(lp).pop(j)
        elif direction_load_d[tp] > 0 and d[tp][0] != 0:
            if straight_line and direction_load_d[lp] > 0 and d[lp][0] != 0:
                ans[d.get(lp)[0]] = timing
                d.get(lp).pop(0)
                direction_load_d[lp] -= 1
                passed += 1
            elif direction_load_d[lp] > 0:
                if d[lp][0] == 0:
                    d.get(lp).pop(0)
                elif (
                    direction_load_d[lp] > 1
                    and len(d.get(lp)) > direction_load_d[lp]
                ):
                    j = 1
                    while d.get(lp)[j] != 0:
                        j += 1
                    d.get(lp).pop(j)
            ans[d.get(tp)[0]] = timing
            passed += 1
            timing += 1

            for priority in priorities[:3]:
                if direction_load_d[priority] > 0:
                    d.get(priority).pop(0)
            direction_load_d[tp] -= 1

        elif direction_load_d[lp] > 0 and d[lp][0] != 0:
            ans[d.get(lp)[0]] = timing
            passed += 1
            timing += 1
            for priority in priorities:
                if direction_load_d[priority] > 0:
                    d.get(priority).pop(0)
            direction_load_d[lp] -= 1
        else:
            for priority in priorities:
                if direction_load_d[priority] > 0:
                    d.get(priority).pop(0)
            timing += 1
    for elem in filter(lambda x: x != 0, ans):
        print(elem)


asserts = False


def main():
    direction_load_d = {x: 0 for x in range(1, 5)}
    if asserts:
        with open("./week03/i_test.txt", "r") as f:
            n = int(f.readline())
            d = {x: [0] * 200 for x in range(1, 5)}
            a, b = map(int, f.readline().split())
            for i in range(1, n + 1):
                direction, arrival_time = map(int, f.readline().split())
                d[direction][arrival_time - 1] = i
                direction_load_d[direction] += 1
    else:
        n = int(input())
        d = {x: [0] * 200 for x in range(1, 5)}
        a, b = map(int, input().strip().split())
        for i in range(1, n + 1):
            direction, arrival_time = map(int, input().strip().split())
            d[direction][arrival_time - 1] = i
            direction_load_d[direction] += 1

    rovers(n, d, direction_load_d, a, b)


if __name__ == "__main__":
    main()
