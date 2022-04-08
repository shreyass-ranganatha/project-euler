import math


def isnum(N):
    return int(N) == N


def ispent(N):
    return isnum((1 + (1 + 24*N)**.5)/6)


def ishexa(N):
    return isnum((1 + (1 + 8*N)**.5)/4)


def istrin(N):
    return isnum((-1 + (1 + 8*N)**.5)/2)


def main():
    tn = lambda N: N*(N + 1)//2

    i = 285
    while 1:
        i += 1

        if ishexa(t := tn(i)) and ispent(t):
            return t


if __name__ == '__main__':
    print(main())
