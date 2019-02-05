# CCC '18 J3 - Are we there yet?

def areWeThereYet(d1, d2, d3, d4):
    dist1 = 0, d1, d1+d2, d1+d2+d3, d1+d2+d3+d4 
    dist2 = [d1, 0, d2, d2+d3, d2+d3+d4]
    dist3 = [d1+d2, d2, 0, d3, d3+d4]
    dist4 = [d1+d2+d3, d2+d3, d3, 0, d4]
    dist5 = [d1+d2+d3+d4, d2+d3+d4, d3+d4, d4, 0]

    return " ".join(str(i) for i in dist1) + "\n" + \
            " ".join(str(i) for i in dist2) + "\n" + \
            " ".join(str(i) for i in dist3) + "\n" + \
            " ".join(str(i) for i in dist4) + "\n" + \
            " ".join(str(i) for i in dist5)

inputArr = str(input()).split(' ')

print(areWeThereYet(int(inputArr[0]), int(inputArr[1]), int(inputArr[2]), int(inputArr[3])))
