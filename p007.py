

def isprime(n):
    if n%2 == 0:
        return 0

    if n%3 == 0 and not n == 3:
        return 0

    if n%5 == 0 and not n == 5:
        return 0

    if n%7 == 0 and not n == 7:
        return 0

    for i in range(11, n, 2):
        if n%i == 0:
            return 0

    return 1


def getprimes():
    i = 2

    while 1:
        if isprime(i):
            yield i
        i += 1


def main():
    pms = getprimes()

    for i in range(10001):
        print(next(pms))


if __name__ == '__main__':
    main()
