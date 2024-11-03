def rude(s, n, c):
    l = r = bestl = bestr = 0
    d = {"a": 0, "b": 0}
    cur_rude = 0
    while r < n:
        cyl = s[r]
        d[cyl] = d.get(cyl, 0) + 1
        if cyl == "b":
            cur_rude += d["a"]
        if cur_rude <= c:
            if r - l >= bestr - bestl:
                bestl, bestr = l, r
        else:
            while cur_rude > c:
                cyl = s[l]
                l += 1
                if cyl == "a":
                    cur_rude -= d["b"]
                d[cyl] -= 1
        r += 1

    return bestr - bestl + 1


assert rude("bbbakbbbabazaababbbaabbbaybaabbaabababbbbbaabbaabb", 50, 0) == 7
assert (
    rude("aaabaababaabaaaabaabbxaazbaaaababaababbbaaaabaabbb", 50, 159) == 39
)
assert rude("aabbbbbaaa", 10, 2) == 8
assert rude("aabbbbbaaa", 10, 1) == 8
assert rude("aabbaaabbbaaa", 13, 6) == 8
assert rude("aab", 3, 1) == 2
assert rude("aabcbb", 6, 2) == 4
assert rude("baaaaaaa", 8, 0) == 8
assert rude("baaaaaaa", 8, 1) == 8
assert rude("abaaaaaaa", 9, 1) == 9
assert rude("abaaa", 5, 0) == 4
assert rude("a", 1, 0) == 1
assert rude("a", 1, 1) == 1
assert rude("b", 1, 0) == 1
assert rude("b", 1, 1) == 1


def main():
    n, c = map(int, input().split())
    string = input()
    print(rude(string, n, c))


if __name__ == "__main__":
    main()
