import math


def factsum(m):
    sm = 0

    while m:
        sm += math.factorial(m % 10)
        m //= 10
    return sm


sm = 0
for i in range(10, 100_000):
    if i == factsum(i):
        print(i)
        sm += i
print(sm)
