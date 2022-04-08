

def makenumber(ar):
    rs = 0

    for i, n in enumerate(ar[::-1]):
        rs += (10**i) * n
    return rs


ds = 2, 3, 5, 7, 11, 13, 17
count = ()


def dowork(ar=tuple(range(10)), rt=()):
    global count

    if len(ar) == 1 and makenumber(rt[-2:] + (ar[0],)) % 17 == 0:
        count += (makenumber(rt + (ar[0],)),)

    for i, n in enumerate(ar):
        if len(rt) == 3 and not n % 2 == 0:
            continue

        if len(rt) == 4 and not makenumber(rt[-2:] + (n,)) % 3 == 0:
            continue

        if len(rt) == 5 and not n % 5 == 0:
            continue

        if len(rt) == 6 and not makenumber(rt[-2:] + (n,)) % 7 == 0:
            continue

        if len(rt) == 7 and not makenumber(rt[-2:] + (n,)) % 11 == 0:
            continue

        if len(rt) == 8 and not makenumber(rt[-2:] + (n,)) % 13 == 0:
            continue

        dowork(ar[:i] + ar[i+1:], rt + (n,))


def main():
    dowork()

    print(count)

    assert 1406357289 in count
    print(sum(count))


if __name__ == '__main__':
    main()
