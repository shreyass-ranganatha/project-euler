import math


def isprime(N):
    if N < 2:
        return 0

    if N % 2 == 0 and not N == 2:
        return 0

    for i in range(3, int(math.sqrt(N))+1, 2):
        if N % i == 0:
            return 0
    return 1


def main():
    lm, mx = 1_000_000, 41
    L = [2]

    for i in range(3, lm, 2):
        if isprime(i):
            L.append(i)

    for i in range(len(L)):
        for j in range(i):
            if (sm := sum(L[j:i])) > lm:
                break

            if sm < mx:
                break

            if isprime(sm) and sm > mx:
                mx = sm

    return mx


if __name__ == '__main__':
    print(main())
