


def is_triangle_word(wrd):
    ar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cs = 0
    for c in wrd:
        cs += ar.index(c) + 1

    # cs*2 = n**2 + n
    # n**2 + n - cs*2 = 0

    # n**2 + n - 100 = 0

    detr = pow(1 + 4*2*cs, .5)

    if int(detr) == detr and detr % 2 == 1:
        return 1

    return 0


def main():
    with open("p42_words.txt") as fo:
        dt = eval(fo.read())

    ct = 0
    for s in dt:
        ct += is_triangle_word(s)

    return ct


if __name__ == '__main__':
    print(main())
