

def gettrips():
    for i in range(1, 999):
        for j in range(i+1, 999):
            c = (i**2 + j**2) ** .5

            if c == int(c):
                yield i, j, int(c)


if __name__ == '__main__':
    gt = gettrips()

    while 1:
        a, b, c = next(gt)

        if sum((a,b,c)) == 1000:
            print(a * b * c)
            break
