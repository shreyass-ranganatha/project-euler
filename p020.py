

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def sums_of_digits(n):
    return sum(int(_) for _ in str(n))


print(sums_of_digits(factorial(100)))
