# CCC '18 J2 - Occupy parking

def occupyParking(n, p1, p2):
    numOccupy = 0
    for i in range(n):
       if (p1[i] == "C" and p2[i] == "C"):
           numOccupy += 1
    return numOccupy

n = int(input())
p1 = input()
p2 = input()

print(occupyParking(n, p1, p2))