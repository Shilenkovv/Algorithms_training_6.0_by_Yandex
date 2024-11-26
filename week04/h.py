from collections import defaultdict
from time import time
# import memory_profiler


# @profile
def optimize_cost(n, edges, costs):
    if n == 1:
        return [costs[0], 1], [1]
    tree = defaultdict(list)
    p_c = dict()
    # costs = defaultdict(list)
    # prices = defaultdict(int)
    # checked = set()
    # for i, elem in enumerate(costs_lst, 1):
    # costs[elem].append(i)
    # prices[i] = elem
    for edge in edges:
        tree[edge[0]].append(edge[1])
        # neighbors[edge[1]].append(edge[0])
    # leaves = deque(i for i in range(1, n + 1) if i not in tree)
    del edges
    # costs_lst.sort(reverse=True)
    # marked = set(range(1, n + 1))
    # total_cost = 0
    negative_marked = set()
    for el in range(n, 0, -1):
        if el not in tree:
            p_c[el] = (
                (costs[el - 1], set([el])),
                (0, set()),
            )
        else:
            positive_cost = costs[el - 1]
            negative_cost = 0
            positive_marked = set([el])
            for child in tree[el]:
                ch_data = p_c[child]
                if ch_data[1][0] < ch_data[0][0]:
                    positive_cost += ch_data[1][0]
                    positive_marked.update(ch_data[1][1])
                else:
                    positive_cost += ch_data[0][0]
                    positive_marked.update(ch_data[0][1])
                negative_cost += ch_data[0][0]
                negative_marked = set(ch_data[0][1])
                p_c.pop(child)
            p_c[el] = (
                (positive_cost, positive_marked.copy()),
                (negative_cost, negative_marked.copy()),
            )
            negative_marked.clear()
            positive_marked.clear()
            # tree.pop(el)
        # print(f"debug {p_c}")
    # print(f"{n = }")  # ! debug
    # print(p_c[1])
    if p_c[1][0][0] < p_c[1][1][0]:
        return [p_c[1][0][0], len(p_c[1][0][1])], list(p_c[1][0][1])
    return [p_c[1][1][0], len(p_c[1][1][1])], list(p_c[1][1][1])


asserts = False
debug_mode = False
stress_test = False


def main():
    if asserts:
        if not stress_test:
            FILENAME = "h_test.txt"
            N_TESTS = 7
        else:
            FILENAME = "h_stress_test.txt"
            N_TESTS = 1
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
                    if n > 1:
                        edges = [
                            tuple(map(int, f.readline().strip().split()))
                            for _ in range(n - 1)
                        ]
                    else:
                        edges = []
                    costs = list(map(int, f.readline().strip().split()))
                    # costs = {i: elem for i, elem in enumerate(costs, 1)}
                    correct_answer = list(
                        map(int, f.readline().strip().split())
                    )
                    correct_nodes = list(
                        map(int, f.readline().strip().split())
                    )
                    s = time()
                    answer, nodes = optimize_cost(n, edges, costs)
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
                        except Exception as e:
                            passed = "FAILED"
                            cur_test = "-"
                            print(e)
                        if len(nodes) < 1000:
                            print(
                                f"test # {i} - {passed} | got {answer}, {nodes} expected {correct_answer}, {correct_nodes}"
                            )
                        else:
                            print(answer)
                        print("---------------------------------")
                        tests_result += cur_test
                except Exception as e:
                    print(e)
                    raise Exception(e)
                    break
            print(f"[{tests_result}]")
    else:
        n = int(input())
        if n > 1:
            edges = [tuple((map(int, input().split()))) for _ in range(n - 1)]
        else:
            edges = []
        costs = list(map(int, input().split()))
        answer, nodes = optimize_cost(n, edges, costs)
        print(" ".join(map(str, answer)), " ".join(map(str, nodes)), sep="\n")


if __name__ == "__main__":
    main()
