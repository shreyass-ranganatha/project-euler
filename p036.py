

def ispalindrome(s):
    if len(s) % 2 == 0:
        return s[len(s)//2:] == s[:len(s)//2][::-1]
    return s[len(s)//2:] == s[:len(s)//2 + 1][::-1]


def is_double_palindromic(m):
    if not ispalindrome(str(m)):
        return 0

    if not ispalindrome(str(bin(m))[2:]):
        return 0

    return 1


sm = 0
for i in range(1, 1_000_000):
    if is_double_palindromic(i):
        sm += i
        print(i)

print('\n', sm)
