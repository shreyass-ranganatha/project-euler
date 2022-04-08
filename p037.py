import math


def isprime(m):
    if m < 2:
        return 0

    if m % 2 == 0 and not m == 2:
        return 0

    for i in range(3, int(math.sqrt(m))+1, 2):
        if m % i == 0:
            return 0
    return 1


def istruncatable(m):
    m = str(m)
    for i in range(len(m)):
        if not isprime(int(m[i:])):
            return 0

        if not isprime(int(m[:len(m)-i])):
            return 0
    return 1


def main():
    sm = 0
    ct = 0

    i = 10
    while ct < 11:
        if istruncatable(i):
            ct += 1
            sm += i
        i += 1

    return sm


if __name__ == '__main__':
    print(main())
