def add(tree: list, n: int) -> list:
    if tree[0] is None:
        tree = [n, None, None]
        print("DONE")
        return tree
    elif tree[0] == n:
        print("ALREADY")
        return tree
    elif n < tree[0]:
        if tree[1] is None:
            tree[1] = [n, None, None]
            print("DONE")
            return tree
        else:
            tree[1] = add(tree[1], n)
    elif n > tree[0]:
        if tree[2] is None:
            tree[2] = [n, None, None]
            print("DONE")
            return tree
        else:
            tree[2] = add(tree[2], n)
    return tree


def search(tree: list, n: int) -> str:
    if tree[0] is None:
        return "NO"
    elif tree[0] == n:
        return "YES"
    elif tree[1] is not None and n < tree[0]:
        return search(tree[1], n)
    elif tree[2] is not None and n > tree[0]:
        return search(tree[2], n)
    return "NO"


def printtree(tree: list, n=0) -> None:
    if tree[1] is not None:
        printtree(tree[1], n + 1)
    print("." * n, tree[0], sep="")
    if tree[2] is not None:
        printtree(tree[2], n + 1)


debug = False
asserts = False


def main():
    main_tree = [None]
    for _ in range(1000):
        try:
            command = input()
            if command == "PRINTTREE":
                printtree(main_tree)
            elif command == "STOP":
                print("Exiting programm")
                break
            else:
                try:
                    command, n = command.split()
                    n = int(n)
                except Exception:
                    print("WRONG COMMAND, EXITING PROGRAMM")
                    break
                if command == "ADD":
                    main_tree = add(main_tree, n)
                elif command == "SEARCH":
                    print(search(main_tree, n))
        except Exception:
            break
        if debug:
            print(f"{main_tree =}")  # ! debug


if __name__ == "__main__":
    main()


# На запрос PRINTTREE надо выводить дерево, обязательно согласно такому алгоритму:

# 1) Распечатать левое поддерево

# 2) Вывести количество точек, равное глубине узла

# 3) Вывести значение ключа

# 4) Распечатать правое поддерево
