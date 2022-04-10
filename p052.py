

def ispermutation(*args):
    srt = sorted(str(args[0]))

    return all(map(
        lambda _: sorted(_) == srt,
        (str(_) for _ in args[1:])
    ))


def main():
    for i in range(1, 10_00_000):
        if ispermutation(i, 2*i, 3*i, 4*i, 5*i, 6*i):
            return i


if __name__ == '__main__':
    print(main())
