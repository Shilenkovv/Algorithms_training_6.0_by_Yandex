import sys
from collections import defaultdict
from time import time

sys.setrecursionlimit(500000)


def money(n: int, managers: list):
    if n == 1:
        return [1]

    total_employees = {1: n - 1}
    tree = defaultdict(list)

    for i, manager in enumerate(managers, start=2):
        tree[manager].append(i)

    def dfs(employee):
        count = 0
        for subordinate in tree[employee]:
            count += 1 + dfs(subordinate)
        total_employees[employee] = count
        return count

    dfs(1)

    coins = [0] * (n + 1)
    for empl in range(n, 0, -1):
        direct_sum = 0
        if tree.get(empl):
            for sub in tree.get(empl):
                direct_sum += coins[sub]
        coins[empl] = 1 + total_employees.get(empl, 0) + direct_sum

    return coins[1:]


asserts = False
debug_mode = False
N_TESTS = 12


def main():
    if asserts:
        FILENAME = "f_test.txt"
        DIR = "./" + FILENAME
        if debug_mode:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "04":
                DIR = "./week04/" + FILENAME

        with open(DIR, "r") as f:
            tests_result = ""
            for i in range(1, N_TESTS + 1):
                try:
                    n = int(f.readline().strip())
                    managers = list(map(int, f.readline().strip().split()))
                    correct_answer = list(
                        map(int, f.readline().strip().split())
                    )
                    s = time()
                    answer = money(n, managers)
                    e = time()
                    print(f"{e - s:.7f} seconds")
                    if asserts:
                        passed = "PASSED"
                        cur_test = "+"
                        try:
                            assert answer == correct_answer
                        except Exception:
                            passed = "FAILED"
                            cur_test = "-"
                        if len(answer) < 10:
                            print(
                                f"test # {i} - {passed} | {n}, {managers}; got {answer}, expected {correct_answer}"
                            )
                        else:
                            print(f"test # {i} - {passed}")
                        print("---------------------------------")
                        tests_result += cur_test
                except Exception as e:
                    print(e)
                    break
            print(f"[{tests_result}]")
    else:
        n = int(input())
        managers = list(map(int, input().split()))
        print(" ".join(map(str, money(n, managers))))


if __name__ == "__main__":
    main()
