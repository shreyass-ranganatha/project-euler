import functools


@functools.cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


@functools.cache
def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))


def ofcount(N):
    count = 0

    for r in range(0, N+1):
        if combinations(N, r) >= 1_000_000:
            count += 1
    return count


def main():
    count = 0

    for n in range(1, 100+1):
        count += ofcount(n)
    return count


if __name__ == '__main__':
    print(main())
