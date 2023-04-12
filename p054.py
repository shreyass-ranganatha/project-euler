
ranks = (
    "high-card",
    "one-pair",
    "two-pairs",
    "three-of-a-kind",
    "straight",
    "flush",
    "full-house",
    "four-of-a-kind",
    "straight-flush",
    "royal-flush"
)
cardvalues = '23456789TJQKA'


def rank(cards):
    suits = [_[1] for _ in cards]
    ssuits = set(suits)

    values = sorted([_[0] for _ in cards], key=lambda _: cardvalues.index(_))
    svalues = set(values)

    if ssuits == {*'TJQKA'}:
        return ranks[-1], values[-1]

    elif (
        len(ssuits) == 1 and
        len(svalues) == 5 and
        cardvalues.index(values[-1]) - cardvalues.index(values[0]) == 4
    ):
        return ranks[-2], values[-1]

    elif (
        len(svalues) == 2 and
        any([True if 4 == values.count(v) else False for v in svalues])
    ):
        for v in svalues:
            if not values.count(v) == 4:
                continue

            return ranks[-3], v

    elif (
        len(svalues) == 2 and
        any([True if 3 == values.count(v) else False for v in svalues]) and
        any([True if 2 == values.count(v) else False for v in svalues])
    ):
        for v in svalues:
            if not values.count(v) == 3:
                continue

            return ranks[-4], v

    elif (
        len(ssuits) == 1
    ):
        return ranks[-5], values[-1]

    elif (
        len(svalues) == 5 and
        cardvalues.index(values[-1]) - cardvalues.index(values[0]) == 4
    ):
        return ranks[-6], values[-1]

    elif (
        any([True if 3 == values.count(v) else False for v in svalues])
    ):
        for v in svalues:
            if not values.count(v) == 3:
                continue

            return ranks[-7], v

    elif (
        len(svalues) == 3 and
        any([True if 2 == values.count(v) else False for v in svalues])
    ):
        for v in values[::-1]:
            if not values.count(v) == 2:
                continue

            return ranks[-8], v

    elif (
        any([True if 2 == values.count(v) else False for v in svalues])
    ):
        for v in values:
            if not values.count(v) == 2:
                continue

            return ranks[-9], v

    else:
        return ranks[-10], values[-1]


def compare(p1, p2) -> bool:
    """True = p1 wins
    False = p2 wins
    """

    cards1 = []
    for cd in p1.split():
        cards1.append(tuple(cd))

    cards2 = []
    for cd in p2.split():
        cards2.append(tuple(cd))

    r1, h1 = rank(cards1)
    r2, h2 = rank(cards2)

    if not r1 == r2:
        return ranks.index(r1) > ranks.index(r2)

    if not h1 == h2:
        return cardvalues.index(h1) > cardvalues.index(h2)

    v1 = sorted(tuple({_[0] for _ in cards1}), key=lambda _: cardvalues.index(_), reverse=1)
    v2 = sorted(tuple({_[0] for _ in cards2}), key=lambda _: cardvalues.index(_), reverse=1)

    for a, b in zip(v1, v2):
        if cardvalues.index(a) == cardvalues.index(b):
            continue

        return cardvalues.index(a) > cardvalues.index(b)


def main():
    ar = [
        ("5H 5C 6S 7S KD", "2C 3S 8S 8D TD"),
        ("5D 8C 9S JS AC", "2C 5C 7D 8S QH"),
        ("2D 9C AS AH AC", "3D 6D 7D TD QD"),
        ("4D 6S 9H QH QC", "3D 6D 7H QD QS"),
        ("2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D"),
    ]

    ar = []
    with open("p054_poker.txt") as fp:
        for ln in fp:
            ln = ln.strip().split()

            ar.append((
                ' '.join(ln[:5]),
                ' '.join(ln[5:])
            ))

    sm = 0
    for p1, p2 in ar:
        sm += compare(p1, p2)

    return sm


if __name__ == '__main__':
    print(main())
