


def get_sums_under(n):
    mso3, mso5 = (n-1)//3, (n-1)//5
    mso15 = (n-1)//15

    so = lambda _: _ * (_+1)//2

    return 3*so(mso3) + 5*so(mso5) - 15*so(mso15)


def main():
    return get_sums_under(1000)


if __name__ == '__main__':
    print(main())
