import functools
import math


def ndivs(n):
    r = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            r += (1 if n/i == i else 2)
    return r


@functools.cache
def sumto(n):
    if n < 1:
        return 0
    return n + sumto(n-1)


def trinumbers():
    i = 1

    while 1:
        yield sumto(i)
        i += 1


tris = trinumbers()

mx = 0
while 1:
    tr = next(tris)
    nd = ndivs(tr)

    if nd > mx:
        mx = nd
        print(tr, mx)

    if nd >= 500:
        break
