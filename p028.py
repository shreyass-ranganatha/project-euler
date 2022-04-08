

sm = 1
sz = 1001
pv = 1
for i in range(1, sz//2 + 1):
    for j in range(4):
        pv += 2*i
        sm += pv

print(sm)
