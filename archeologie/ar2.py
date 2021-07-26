import time
with open("ar2.in", "r") as file:
	data = [[y for y in x] for x in file.read().split("\n")]


outDat = data[::]

# def findNeighbors(x: int, y: int, furthest: int) -> int:
# 	data[y][x] = f"{furthest}"
# 	for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
# 		if y+dy < 0 or y+dy > len(data): continue
# 		if x+dx < 0 or x+dx > len(data[0]): continue
# 		if data[y + dy][x + dx] == " ":
# 			data[y + dy][x + dx] = f"{furthest+1}"
# 			outDat[y+dy][x+dx] = furthest
# 			dist = findNeighbors(x + dx, y + dy, furthest+1)
# 			if dist > furthest: furthest = dist
# 	return furthest


# print(findNeighbors(1, 1, 0), "furthest")

# # output
# output: list[str] = []
# for row in outDat:
# 	for i, space in enumerate(row):
# 		row[i] = "{:3s}".format(space)
# 	joined = " ".join(row)
# 	output.append(joined)

# with open("ar2.out", "w+") as file:
# 	file.write("\n".join(output))

class Vertex:
	def __init__(this, x: int, y: int, dist: int):
		this.x = x
		this.y = y
		this.dist = dist
	def findNeighbors(this):
		return findNeighbors(this)

def findNeighbors(v: Vertex) -> list[Vertex]:
	neigh: list[Vertex] = []
	for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		if v.x+dx > len(data[0]) or v.x+dx < 0: continue
		if v.y+dy > len(data) or v.y+dy < 0: continue
		neigh.append(Vertex(v.x+dx, v.y+dy, v.dist+1))
	return neigh

visited: list[Vertex] = []


def checkIfVisited(toCheck: Vertex):
	for vertex in visited:
		if vertex.x == toCheck.x and vertex.y == vertex.y: return True
	return False

def bfs(start: Vertex):
	global visited
	visited.append(start)
	queue = [start]

	while queue:
		current = queue.pop(0)
		print(len(queue), len(visited))
		neighbours = current.findNeighbors()
		for neighbor in neighbours:
			if not checkIfVisited(neighbor):
				visited.append(neighbor)
				queue.append(neighbor)

bfs(Vertex(1, 1, 0))

longest = 0
for v in visited:
	print(v.x, v.y)
	if v.dist > longest: longest = v.dist
print(longest)