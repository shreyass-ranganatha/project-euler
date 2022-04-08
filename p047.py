

def isprime(n):
    if n % 2 == 0 and not n == 2:
        return 0

    if n < 2:
        return 0

    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            return 0
    return 1


def primefactors(n):
    r = []

    while n > 1:
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                if isprime(i):
                    r.append(i)
                    n //= i
                    break
                elif isprime(n//i):
                    r.append(n//i)
                    n //= n//i
                    break

    return set(r)


def main():
    for i in range(1_000_000):
        if all(map(lambda _: len(primefactors(_)) == 4, tuple(range(i, i+3 + 1) ))):
            return i


if __name__ == '__main__':
    print(main())
