

def sum_digits(n):
    sm = 0
    while n > 0:
        sm += n % 10
        n = n//10

    return sm


def main():
    return sum_digits(2**1000)


if __name__ == '__main__':
    print(main())
