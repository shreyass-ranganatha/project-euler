

with open("p22_names.txt", 'r') as f:
    dt = sorted(eval(f.read()))


def getscore(st):
    r = 0

    for c in st:
        r += ord(c) - ord('A') + 1
    return r


sm = 0
for i, v in enumerate(dt):
    sm += getscore(v) * (i+1)

print(sm)
