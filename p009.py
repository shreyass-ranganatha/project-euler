

def gettrips():
    for i in range(1, 999):
        for j in range(i+1, 999):
            c = (i**2 + j**2) ** .5

            if c == int(c):
                yield i, j, int(c)


def main():
    gt = gettrips()

    while 1:
        a, b, c = next(gt)

        if a + b + c == 1000:
            return a * b * c


if __name__ == '__main__':
    print(main())
