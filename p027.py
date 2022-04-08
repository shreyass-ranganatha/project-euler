import math
import functools


@functools.cache
def isprime(n: int):
    if n < 2:
        return False

    if n % 2 == 0 and not n == 2:
        return 0

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0
    return 1


def getprimes(limit):
    rs = []

    for i in range(1, limit):
        if isprime(i):
            rs.append(i)
    return rs


def f(n, a, b):
    return n**2 + a*n + b


def checkequation(a, b):
    cnt = 0

    for i in range(0, a if a>b else b):
        if isprime(f(i, a, b)):
            cnt += 1
        else:
            break
    return cnt



rs = [1] + getprimes(1000)

mx = 0
mv = 0
for a in rs:
    for b in rs:
        if (cq := checkequation(a, b)) > mv:
            mv = cq
            mx = a*b

        if (cq := checkequation(-a, b)) > mv:
            mv = cq
            mx = -a*b

        if (cq := checkequation(a, -b)) > mv:
            mv = cq
            mx = a*-b

        if (cq := checkequation(-a, -b)) > mv:
            mv = cq
            mx = a*b
print(mx, mv)
