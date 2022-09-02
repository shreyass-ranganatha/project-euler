import math


# ,1
def isprime(n):
    if n <= 1:
        return 0

    if n % 2 == 0 and not n == 2:
        return 0

    # int(math.sqrt(n)) is the bits
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0
    return 1


def sum_primes_under(n):
    sm = 2

    for i in range(3, n, 2):
        if isprime(i):
            sm += i
    return sm


def main():
    return "sum", sum_primes_under(2_000_000)


if __name__ == '__main__':
    print(main())
