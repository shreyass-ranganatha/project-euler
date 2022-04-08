import functools


@functools.cache
def countseq(n):
    if n == 1:
        return 1

    return 1 + countseq(n//2 if n%2 == 0 else (3*n + 1))


def main():
    mx, ix = 0, 0
    for i in range(1, 1_000_000):
        if (c := countseq(i)) > mx:
            mx, ix = c, i

    print(ix)

if __name__ == '__main__':
    main()
