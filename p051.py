

def isprime(N):
    if N < 2:
        return 0

    if N % 2 == 0 and not N == 2:
        return 0

    for i in range(3, int(N ** .5)+1, 2):
        if N % i == 0:
            return 0
    return 1


def checkpattern(N, mx=7):
    N = str(N)
    n = tuple(_ for _ in N[:-1] if int(_) <= (10 - mx))

    for _ in n:
        count = 10 - int(_)

        for z in range(int(_), 9+1):
            if not isprime(vu := int(N[:-1].replace(_, str(z)) + N[-1])):
                count -= 1

            if count < mx:
                break

        if count >= mx:
            return _, count


def main():
    i = 1

    while 1:
        if isprime(i) and checkpattern(i, 8):
            return i
        i += 2


if __name__ == '__main__':
    print(main())
