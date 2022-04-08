import functools


@functools.cache
def isprime(n):
    if n == 1:
        raise ValueError("1 isn't prime nor composite")

    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1


def ntimes(a, b):
    r = []
    while 1:
        if not a%b == 0:
            break

        a //= b
        r.append(b)

    return tuple(r)


def getprimes():
    i = 2

    while 1:
        if isprime(i):
            yield i
        i += 1


def get_prime_factors(n):
    pms = getprimes()

    rs = ()
    while ((ps := next(pms)) <= n):
        rs += ntimes(n, ps)

    return rs


def counts(ar, n):
    return max(ar, key=lambda _: _.count(n)).count(n)


def get_smallest_number_under(n):
    sws = set()

    ar = []
    for i in range(2, n+1):
        ar.append(get_prime_factors(i))
        sws = sws | set(ar[-1])

    rs = 1
    for w in sws:
        rs *= w ** counts(ar, w)

    return rs

if __name__ == '__main__':
    # print(get_prime_factors(9, getprimes()))
    print(get_smallest_number_under(20))
