

def getstring(ar):
    r = ""

    for a in ar:
        r += str(a)
    return r


def main(ar):
    st = getstring(range(1, 1000000+1))

    r = 1
    for a in ar:
        r *= int(st[a-1])

    return r


if __name__ == '__main__':
    print(main((1, 10, 100, 1_000, 10_000, 100_000, 1_000_000)))
    # print(sum(range(1, 10+1))*6)
