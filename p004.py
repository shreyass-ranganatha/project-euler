

def ispalindrome(n):
    return 1 if str(n) == str(n)[::-1] else 0


def submain(a, b):
    for i in range(a, b, -1):
        for j in range(a, b, -1):
            if ispalindrome(i*j):
                yield i*j


def main():
    return max(tuple(submain(999, 99)))


if __name__ == '__main__':
    print(main())
