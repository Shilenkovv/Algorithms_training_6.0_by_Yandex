def build_tree(tree: list, node: str, childrens: dict, debug=True):
    if not tree:
        tree = [node, []]
        while childrens.get(node):
            if tree[-1]:
                tree.append(build_tree([], childrens.get(node)[0], childrens, debug))
            else:
                tree[-1] = build_tree(
                    tree[-1], childrens.get(node)[0], childrens, debug
                )
            if debug:  # ! debug
                print(tree)  # ! debug
            childrens.get(node).pop(0)
        if node in childrens:
            childrens.pop(node)
    return tree


def count_childs(d: dict, tree: list) -> int:
    node = tree[0]
    if len(tree) == 1 or not any(tree[1:]):
        d[node] = 0
        return 0

    total_descendants = 0
    for child in tree[1:]:
        if child:
            total_descendants += 1 + count_childs(d, child)

    d[node] = total_descendants
    return total_descendants


asserts = False
debug = False


def main():
    import sys

    sys.setrecursionlimit(100000)

    if asserts:
        DIR = "./b_test.txt"
        if debug:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "08":
                DIR = "./week08/b_test.txt"
        with open(DIR, "r") as f:
            data = [f.readline().strip() for _ in range(int(f.readline()) - 1)]
    else:
        data = [input() for _ in range(int(input()) - 1)]
    sons, fathers = set(), set()
    childrens = dict()
    if debug:  # ! debug
        print(data)  # ! debug
    for elem in data:
        son, father = elem.split()
        sons.add(son)
        fathers.add(father)
        childrens.setdefault(father, []).append(son)
    start = next(iter(set(fathers.difference(sons))))
    tree = []
    if debug:
        print(f"greatfather = {fathers.difference(sons)}")
        print(childrens)
    tree = build_tree(tree, start, childrens, debug)
    d = {}
    count_childs(d, tree)
    for key in sorted(d):
        print(f"{key} {d.get(key)}")


if __name__ == "__main__":
    main()
