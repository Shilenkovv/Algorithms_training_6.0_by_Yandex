asserts = False
debug_mode = False


def main():
    ancestors_d = dict()
    # data = []
    if asserts:
        FILENAME = "c_test.txt"
        DIR = "./" + FILENAME
        if debug_mode:
            import os

            cwd = os.getcwd()
            if cwd[-2:] != "04":
                DIR = "./week04/" + FILENAME
        with open(DIR, "r") as f:
            n = int(f.readline().strip())
            for i in range(n - 1):
                son, anc = f.readline().strip().split()
                ancestors_d[son] = anc
                # data.append((son, anc))
            for line in f.readlines():
                try:
                    person_a, person_b = line.strip().split()
                except Exception:
                    break
                ancestors_a = set()
                while person_a in ancestors_d:
                    ancestors_a.add(person_a)
                    person_a = ancestors_d[person_a]
                ancestors_a.add(person_a)
                while person_b not in ancestors_a:
                    person_b = ancestors_d[person_b]
                print(person_b)
    else:
        n = int(input().strip())
        for i in range(n - 1):
            son, anc = input().strip().split()
            ancestors_d[son] = anc
            # data.append((son, anc))

        for _ in range(10000):
            try:
                person_a, person_b = input().strip().split()
                ancestors_a = set()
                while person_a in ancestors_d:
                    ancestors_a.add(person_a)
                    person_a = ancestors_d[person_a]
                ancestors_a.add(person_a)
                while person_b not in ancestors_a:
                    person_b = ancestors_d[person_b]
                print(person_b)
            except Exception:
                break


if __name__ == "__main__":
    main()
