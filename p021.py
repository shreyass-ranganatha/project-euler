import math


def d(n):
    r = 1

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            r += i + (n//i) if not n//i == i else 0
    return r


def main():
    sm = 0

    for i in range(1, 10_000):
        if d(d(i)) == i and not i == d(i):
            sm += i
    return sm


print(main())
