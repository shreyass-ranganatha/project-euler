from itertools import permutations, combinations
import math, timeit, functools


@functools.cache
def toint(ar):
    rs = 0
    for i, v in enumerate(ar):
        rs = rs*10 + v

    return rs


def isprime(n):
    if n % 2 == 0 and not n == 2:
        return 0

    if n < 2:
        return 0

    for i in range(3, int(n ** .5)+1, 2):
        if n % i == 0:
            return 0
    return 1


def perms(n):
    return tuple(toint(__) for __ in permutations((int(_) for _ in str(n)), 4) if not toint(__) < 1000)


def main():
    for i in range(1489, 9999+1, 2):
        if not isprime(i):
            continue

        pms = perms(i)

        if isprime(i + 3330) and isprime(i + 2*3330) and (i + 3330) in pms and (i + 2*3330) in pms:
            return str(i) + str(i + 3330) + str(i + 2*3330)




if __name__ == '__main__':
    print(main())
