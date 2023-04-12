import itertools
import functools

@functools.cache
def digitsum(N):
    sm = 0

    while N:
        sm += N % 10
        N //= 10
    return sm


def main():
    mx = None

    for a, b in itertools.permutations(range(90, 100), 2):
        if mx is None or digitsum(a ** b) > mx:
            mx = digitsum(a ** b)
    return mx


if __name__ == '__main__':
    print(main())
