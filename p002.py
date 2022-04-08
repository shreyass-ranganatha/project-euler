

def sums_of_fibonacci(n, a=1, b=2):
    if a+b >= n:
        return (a if a%2 == 0 else 0) + (b if b%2 == 0 else 0)

    return (a if a%2 == 0 else 0) + sums_of_fibonacci(n, b, a+b)


def main():
    return sums_of_fibonacci(4_000_000)


if __name__ == '__main__':
    print(main())
