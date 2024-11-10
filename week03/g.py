def pwz(n: int, b: int, customers: list) -> int:
    tot_customers = minutes = 0
    for i in range(n):
        tot_customers += customers[i]
        minutes += tot_customers
        tot_customers -= min(tot_customers, b)
    minutes += tot_customers
    return minutes


# from time import time

# s = time()
# assert pwz(3, 4, [1, 5, 9]) == 22
assert pwz(5, 4, [5, 5, 0, 0, 10]) == 29
assert pwz(5, 10, [11, 11, 11, 11, 11]) == 70
assert pwz(5, 10, [5, 5, 5, 5, 5]) == 25
assert pwz(1, 10, [5]) == 5
assert pwz(1, 10, [25]) == 40
# print(f"first test {time() - s}s.")
# s = time()
# print(pwz(10**5, 1, [10**8] * 10**5))
# print(f"second test {time() - s}s.")
# s = time()
# print(pwz(10**5, 10**7, [10**8] * 10**5))
# print(f"third test {time() - s}s.")


# 1 <= n <= 100 000
# 1 <= b <= 10 ** 8
# 0 <= ai <= 10 ** 8


def main():
    n, b = map(int, input().split())
    customers = list(map(int, input().split()))
    print(pwz(n, b, customers))


if __name__ == "__main__":
    main()
