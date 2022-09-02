import functools


@functools.cache
def getnpaths(a, b):
    if a == b == 0:
        return 1

    return \
        (getnpaths(a-1, b) if a-1 >= 0 else 0) + \
        (getnpaths(a, b-1) if b-1 >= 0 else 0)


def main():
    return getnpaths(20, 20)


if __name__ == '__main__':
    print(main())
