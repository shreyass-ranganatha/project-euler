import math


st = set(str(_) for _ in range(1, 9+1))


def ispand(m):
    return len(m) == 9 and (st & set(m)) == st


rs = []
sm = 0
for a in range(1234, 9876):
    for b in range(1, int(math.sqrt(a))+1):
        if a % b == 0:
            if ispand(str(a) + str(b) + str(a//b)):
                rs.append((a, b, a//b))
                sm += a

                break

print(len(rs))
print(sm)
