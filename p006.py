

def sum_of_squares(n):
    sm = 0
    for i in range(1, n+1):
        sm += i**2

    return sm


def square_of_sum(n):
    sm = 0
    for i in range(1, n+1):
        sm += i

    return sm**2


def main():
    n = 100
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == '__main__':
    print(main())
