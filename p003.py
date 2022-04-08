import functools


@functools.cache
def isprime(n):
    if n == 1:
        raise ValueError("1 is neither prime nor composite")

    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1


@functools.cache
def getprimes():
    i = 2

    while 1:
        if isprime(i):
            yield i
        i += 1


def ntimes(a, b):
    r = []
    while 1:
        if not a%b == 0:
            break

        a //= b
        r.append(b)

    return a, tuple(r)


def retr_prime_factors(n, p=2, ps=()):
    a, b = n, ()

    while a > 1:
        a, c = ntimes(a, next(getprimes()))
        b += c
    return b


def main():
    return retr_prime_factors(600851475143)


if __name__ == '__main__':
    print(main())
