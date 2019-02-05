# CCC '18 J1 - Telemarketer or not?

def telephone(a, b, c, d):
    if (a != 8 and a != 9):
        return "answer"
    elif (d != 8 and d != 9):
        return "answer"
    elif (b != c):
        return "answer"
    else:
        return "ignore"

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print(telephone(n1, n2, n3, n4))