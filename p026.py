


def divides(n, nm=1):
    seqn = ()
    store = {}

    while 1:
        if nm not in store:
            if nm >= n:
                store[nm] = str(nm//n)
                seqn += (nm,)
                nm %= n

            else:
                nm *= 10

            if nm == 0:
                break

        else:
            return seqn[seqn.index(nm):]


mx, mv = 0, 0
for i in range(1, 1000):
    if (dv := divides(i)):
        if len(dv) > mv:
            mx = i
            mv = len(dv)

print(mx, mv)
