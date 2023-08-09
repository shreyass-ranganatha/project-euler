import math


def main():
    n, d = 3, 2
    c = 0
    r = [0]

    for i in range(1000):
        n = n + d * 2
        d = n - d

        r.append(0)

        if int(math.log10(n)) > int(math.log10(d)):
            c += 1
            r[-1] = 1
    return c


if __name__ == '__main__':
    print(main())
