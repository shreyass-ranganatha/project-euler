

def digitpws(n, pw):
    sm = 0

    for a in str(n):
        sm += int(a)**pw

        if sm > n:
            break
    return sm


# for i in range(10, 1_000_000):
#     if digitpws(i, 4) == i:
#         print(i)

sr = """4150
4151
54748
92727
93084
194979"""
print(sum(tuple(int(_) for _ in sr.split())))
