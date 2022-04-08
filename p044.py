import functools
import math


def ispentagonal(N):
    return (lambda _: int(_) == _)((1 + (1 + 24*N)**.5)/6)


def main():
    pn = functools.cache(lambda N: N * (3*N - 1)//2)

    i = 2
    while 1:
        for j in range(i-1, 0, -1):
            if ispentagonal(sm := (pn(i) + pn(j)) ) and ispentagonal(df := int(math.fabs(pn(i) - pn(j))) ):
                return df

        i += 1

if __name__ == '__main__':
    print(main())
