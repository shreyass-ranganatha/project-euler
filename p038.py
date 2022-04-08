

def decent(m):
    for _ in m:
        if m.count(_) > 1:
            return 0
    return 1


def ispandigital(m):
    if '0' in m:
        return False

    if not len(set('123456789') & set(m)) == 9:
        return False
    return True


def sum(ar):
    if len(ar) == 1:
        return ar[0]
    return ar[0] + sum(ar[1:])


def build(m):
    i = 1

    r = ""
    while 1:
        r += str(m * i)

        if not decent(r):
            return

        if ispandigital(r):
            return i, r

        i += 1


def main():
    mx = 0
    for i in range(1_000_000):
        r = build(i)

        if r:
            j, v = r
            v = int(v)
            mx = v if v > mx else mx

            print(i, j, v)

    print("Max", mx)
