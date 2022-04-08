

def last10s(n):
    sm = 0
    for i in range(1, n+1):
        sm += i**i

    return str(sm)[-10:]


def main():
    return last10s(1000)


if __name__ == '__main__':
    print(main())
