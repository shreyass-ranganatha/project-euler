

digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

teens = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def towords(n):
    if n == 0:
        return "zero"

    if n in digits:
        return digits[n]

    if n in teens:
        return teens[n]

    if n in tens:
        return tens[n]

    s = str(n)

    if len(s) == 2:
        return ' '.join((tens[int(s[0])*10], digits[int(s[1])]))

    if len(s) == 3:
        return ' '.join((digits[int(s[0])], "hundred and", towords(int(s[1:]))))

    return "one thousand"


def sums_of(n):
    sm = 0

    for i in range(1, n+1):
        sm += len(towords(i).replace(' ', ''))

    return sm

print(sums_of(1000)) # should be 21124
# print(towords(915))
