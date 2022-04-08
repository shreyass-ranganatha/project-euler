

rs = set()
mx = 100

for a in range(2, mx+1):
    for b in range(2, mx+1):
        rs |= {a**b}

print(len(rs))
