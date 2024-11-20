import sys

sys.setrecursionlimit(100000)


def build_tree(tree: list, node: str, childrens: dict, debug=True):
    if not tree:
        tree = [node, []]
        while childrens.get(node):
            if tree[-1]:
                tree.append(
                    build_tree([], childrens.get(node)[0], childrens, debug)
                )
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


def LCA(tree: list, person_a: str, person_b: str) -> str:
    if not tree:
        return None

    if tree[0] == person_a or tree[0] == person_b:
        return tree[0]

    ancestors = []
    for child in tree[1:]:
        ancestor = LCA(child, person_a, person_b)
        if ancestor:
            ancestors.append(ancestor)

    if len(ancestors) == 2:
        return tree[0]

    return ancestors[0] if ancestors else None


asserts = False
debug = False


def main():
    if asserts:
        FILENAME = "c_test.txt"
        DIR = "./" + FILENAME
        if debug:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "04":
                DIR = "./week04/" + FILENAME
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
    if asserts:
        with open(DIR, "r") as f:
            for _ in range(int(f.readline()) - 1):
                f.readline()
            for _ in range(1000000):
                try:
                    person_a, person_b = f.readline().strip().split()
                    print(LCA(tree, person_a, person_b))
                except Exception as e:
                    if debug:
                        print(e)
                    break
    else:
        for _ in range(1000000):
            try:
                person_a, person_b = input().split()
                print(LCA(tree, person_a, person_b))
            except Exception as e:
                if debug:
                    print(e)
                break


if __name__ == "__main__":
    main()
