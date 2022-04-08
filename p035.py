import functools
import math


@functools.cache
def isprime(m):
    if m % 2 == 0 and not m == 2:
        return 0

    for i in range(3, int(math.sqrt(m))+1, 2):
        if m % i == 0:
            return 0
    return 1


def iscircular(m):
    if not isprime(m):
        return 0

    m = str(m)

    for i in range(len(m)):
        r = m[i:] + m[:i]

        if not isprime(int(r)):
            return 0
    return 1


ct = 0
for i in range(2, 1_000_000):
    if iscircular(i):
        ct += 1
        print(i)

print()
print(ct)
