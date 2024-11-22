from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def compute_subtree_size(n, data):
    graph = defaultdict(list)
    for u, v in data:
        graph[u].append(v)
        graph[v].append(u)

    subtree_size = [0] * (n + 1)

    def dfs(node, parent):
        subtree_size[node] = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]

    dfs(1, -1)

    return subtree_size[1:]


asserts = False
debug_mode = False


def main():
    if asserts:
        FILENAME = "e_test.txt"
        DIR = "./" + FILENAME
        if debug_mode:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "04":
                DIR = "./week04/" + FILENAME
        with open(DIR, "r") as f:
            data = [
                tuple(map(int, f.readline().strip().split()))
                for _ in range(int(f.readline()) - 1)
            ]
    else:
        data = [
            tuple(map(int, input().split())) for _ in range(int(input()) - 1)
        ]

    result = compute_subtree_size(len(data) + 1, data)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
