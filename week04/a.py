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


def count_deep(d: dict, tree: list, n: int = 0) -> dict:
    for elem in tree:
        if isinstance(elem, str):
            d.update({elem: n})
        elif elem:
            count_deep(d, elem, n + 1)
    return d


asserts = False
debug = False


def main():
    # n = int(input())
    if asserts:
        DIR = "./a_test.txt"
        if debug:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "08":
                DIR = "./week08/a_test.txt"
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
    d = count_deep(dict(), tree)
    for key in sorted(d):
        print(f"{key} {d.get(key)}")


if __name__ == "__main__":
    main()
