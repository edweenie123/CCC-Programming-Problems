# CCC '18 J5 - Choose your own path

n = int(input())

pageGraph = {}
for i in range(n):
	line = [int(x)-1 for x in input().split(' ')[1:]]
	pageGraph[i] = line

# Use modified version of BFS to check if all nodes are accessable and find the length of shortest path

pagesVisited = 1
foundPath = False
shortestDist = None

queue = [0]
distances = [None] * n
distances[0] = 1
while len(queue) > 0:
	pagePath = queue.pop(0)
	if len(pageGraph[pagePath]) == 0 and not foundPath:
		# found shortest path to end
		shortestDist = distances[pagePath]
		foundPath = True
	for p in pageGraph[pagePath]:
		if distances[p] == None:
			queue.append(p)
			distances[p] = distances[pagePath] + 1 # distance to node p
			pagesVisited += 1 # counting pages visited

# Outputting answers
if pagesVisited == n:
	print('Y')
else:
	print('N')

print(shortestDist)