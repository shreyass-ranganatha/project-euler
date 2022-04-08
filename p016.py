

def sum_digits(n):
    sm = 0
    while n>0:
        sm += n%10
        n = n//10

    return sm


print(sum_digits(2**1000))
