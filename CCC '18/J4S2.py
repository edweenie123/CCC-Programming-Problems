# CCC '18 J4/S2 - Sunflowers

def getCol(arr, col):
		returnArray = []
		for i in range(len(arr)):
			returnArray.append(arr[i][col])
		return returnArray

def sunflower(arr, n):
	rotArr = arr
	for i in range(4):
		tempArr = list(zip(*rotArr[::-1]))
		rotArr = []
		
		for i in tempArr:
			rotArr.append(list(i))
		isRotated = False
		for j in range(n):
			if rotArr[j] != sorted(rotArr[j]):
				isRotated = True
		
		for j in range(n):
			if getCol(rotArr, j) != sorted(getCol(rotArr, j)):
				isRotated = True

		if isRotated == False:
			return rotArr

n = int(input())
arr=[]
for i in range(n):
	arr.append(input().split(' '))
arr1=[]
for i in arr:
	row = []
	for j in i:
		row.append(int(j))
	arr1.append(row)

rotArr = sunflower(arr1, n)
for i in rotArr:
	line = ""
	for j in i:
		line += str(j) + " "
	print(line)