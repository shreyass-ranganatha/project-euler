

def islychrel(n: int) -> bool:
    r = int(str(n)[::-1])

    for _ in range(50):
        n += r
        r = int(str(n)[::-1])

        if n == r:
            return False
    return True


ct = 0
for n in range(0, 10_000+1):
    ct += islychrel(n)

print(ct)
