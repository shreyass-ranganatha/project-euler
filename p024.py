

ct = 0


def perms(dt, rw=()):
    global ct

    if not dt:
        ct += 1

        if ct == 1_000_000:
            print(ct, rw)
            quit()

    for i, v in enumerate(dt):
        perms(dt[:i] + dt[i+1:], rw + (v,))


ps = perms(tuple(range(10)))
