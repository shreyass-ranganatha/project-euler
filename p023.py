import math


def isperfect(n):
    r = 1

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            r += i + (n//i) if not n//i == i else i
    return -1 if r < n else (0 if r == n else 1)


def upto(n, ar):
    for i, _ in enumerate(ar):
        if _ > n:
            return ar[:i]
    return ar


abs = []

for i in range(1, 28123+1):
    if isperfect(i) > 0:
        abs.append(i)


sm = sum(range(1, 28123))
for i in range(28123):
    ar = upto(i, abs)

    for j in ar[::-1]:
        if (i-j) in ar:
            print(i)
            sm -= i
            break

print(sm)
