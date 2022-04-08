

coins = 200, 100, 50, 20, 10, 5, 2, 1


def counts(m, i=0):
    if i == coins.index(2):
        return 1 * (m//2 + 1)

    ct = 0
    for a in range(m//coins[i] + 1):
        ct += counts(m - (coins[i]*a), i+1)

    return ct


print(counts(200))
