

def build(p):
    r = []

    for i in range(1, p):
        for j in range(i+1, p-i):
            if i**2 + j**2 == (p - i - j)**2:
                r.append((i, j, p-i-j))
    return r


def main():
    mx = 0
    nu = 0
    for i in range(1, 1000+1):
        v = build(i)

        if len(v) > mx:
            mx = len(v)
            nu = i

        print(i, v)

    return (nu, mx)
