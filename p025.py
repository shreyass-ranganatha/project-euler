

def fibonacci():
    a, b = 1, 1
    while 1:
        yield a

        a, b = b, a+b


fb = fibonacci()

i = 1
while 1:
    if len(str(next(fb))) >= 1000:
        print(i)
        break

    i += 1
