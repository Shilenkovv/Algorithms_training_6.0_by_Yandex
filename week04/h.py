from collections import defaultdict
from time import time


def optimize_cost(n, edges, costs_lst):
    neighbors = defaultdict(list)
    costs = defaultdict(list)
    for i, elem in enumerate(costs_lst, 1):
        costs[elem].append(i)
    for edge in edges:
        neighbors[min(edge)].append(max(edge))
        neighbors[max(edge)].append(min(edge))
    marked = set(range(1, n + 1))
    # checked = set()
    # marked = set()
    total_cost = 0
    while costs:
        price = max(costs)
        elem = costs[price][0]
        for neighbor in neighbors[elem]:
            if neighbor not in marked:
                total_cost += price
                # costs.pop(elem)
                # checked.add(elem)
                break
        else:
            marked.remove(elem)
        costs[price].pop(0)
        if not costs[price]:
            costs.pop(price)
        # checked.add(elem)
    answer = [total_cost, len(marked)]
    return answer, sorted(marked)


asserts = True
debug_mode = True
N_TESTS = 3


def main():
    if asserts:
        FILENAME = "h_test.txt"
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
                    edges = [
                        tuple(map(int, f.readline().strip().split()))
                        for _ in range(n - 1)
                    ]
                    costs_lst = list(map(int, f.readline().strip().split()))
                    # costs = {i: elem for i, elem in enumerate(costs, 1)}
                    correct_answer = list(
                        map(int, f.readline().strip().split())
                    )
                    correct_nodes = list(
                        map(int, f.readline().strip().split())
                    )
                    s = time()
                    answer, nodes = optimize_cost(n, edges, costs_lst)
                    e = time()
                    print(f"{e - s:.7f} seconds")
                    if asserts:
                        passed = "PASSED"
                        cur_test = "+"
                        try:
                            assert (
                                answer == correct_answer
                                and nodes == correct_nodes
                            )
                        except Exception:
                            passed = "FAILED"
                            cur_test = "-"
                        print(
                            f"test # {i} - {passed} | got {answer}, {nodes} expected {correct_answer}, {correct_nodes}"
                        )
                        print("---------------------------------")
                        tests_result += cur_test
                except Exception as e:
                    print(e)
                    raise Exception(e)
                    break
            print(f"[{tests_result}]")
    else:
        n = int(input())
        edges = [(map(int, input().split())) for _ in range(n - 1)]
        costs_lst = list(map(int, input().split()))
        # costs = {elem: i for i, elem in enumerate(costs, 1)}
        correct_answer = list(map(int, input().split()))
        correct_nodes = list(map(int, input().split()))

        answer, nodes = optimize_cost(n, edges, costs_lst)
        print(" ".join(map(str, answer)), " ".join(map(str, nodes)), sep="\n")


if __name__ == "__main__":
    main()
