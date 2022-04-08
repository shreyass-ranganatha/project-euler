import math


def isprime(n):
    if n % 2 == 0 and not n == 2:
        return 0

    if n < 2:
        return 0

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0
    return 1


def goldbachs(n):
    if n % 2 == 0:
        return None

    if isprime(n):
        return None

    for i in range(1, int(math.sqrt(n))):
        if isprime(n - 2 * i**2):
            return n - 2 * i**2, i
    return 0


def main():
    i = 3

    while i < 10_000:
        if goldbachs(i) == 0:
            return i
        i += 2


if __name__ == '__main__':
    print(main())
