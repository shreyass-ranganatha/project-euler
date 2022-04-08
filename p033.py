import math


def hcf(a: int, b: int):
    mn, mx = sorted((a, b))

    hf = 1
    for i in range(1, int(math.sqrt(mn))+1):
        if mn % i == 0 and mx % i == 0:
            if mx % (mn//i) == 0:
                hf = mn//i if mn//i > hf else hf

            else:
                hf = i if i > hf else hf
    return hf


def iscurious(a, b):
    a, b = str(a), str(b)
    ch = ''.join(set(a) & set(b))

    if not len(ch) == 1:
        return False

    if ch*2 == a or ch*2 == b:
        return False

    if ch == '0':
        return False

    try:
        if not int(a) / int(b) == int(a.replace(ch, '')) / int(b.replace(ch, '')):
            return False

    except ZeroDivisionError:
        return False

    return True


nm = 1
dm = 1
for i in range(10, 99+1):
    for j in range(i+1, 98+1):
        if iscurious(i, j):
            nm *= i
            dm *= j

print(nm, dm, sep='/')

hf = hcf(nm, dm)
print(nm//hf, dm//hf, sep='/')
