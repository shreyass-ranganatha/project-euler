import math
import itertools as it


def isprime(n):
    if n % 2 == 0 and not n == 2:
        return 0

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0
    return 1


def main():
    k = 7

    for i in it.permutations(range(k, 0, -1), k):
        n = int(''.join(str(_) for _ in i))

        if isprime(n):
            return n


if __name__ == '__main__':
    print(main())
    # print(isprime())
