
def first_sundays_between(yr1, yr2):
    dys, ct = 0, 0

    for yr in range(yr1, yr2+1):
        for mn in range(1, 12+1):
            if (dys+1)%7 == 0:
                ct += 1

            if mn in (9, 11, 6, 8):
                dys += 30
            elif mn == 2:
                dys += 28 + (1 if yr%4 == 0 else 0)

            else:
                dys += 31
    return ct


print(first_sundays_between(1900, 2000))
