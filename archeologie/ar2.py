import time
# with open("ar2.in", "r") as file:
# 	data = [[y for y in x] for x in file.read().split("\n")]

# class Vertex:
# 	def __init__(this, x: int, y: int, dist: int):
# 		this.x = x
# 		this.y = y
# 		this.dist = dist
	# def findNeighbors(this):
	# 	return findNeighbors(this)
	# def get_visited(this):
	# 	return isVisited(this)
	# visited: bool = property(get_visited)

# def findNeighbors(v: Vertex) -> list[Vertex]:
	# neigh: list[Vertex] = []
	# for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
	# 	if v.x+dx > len(data[0]) or v.x+dx < 0: continue
	# 	if v.y+dy > len(data) or v.y+dy < 0: continue
	# 	value = data[v.x+dx][v.y+dy]
	# 	if value != " ": continue
	# 	print(v.y, v.x)
	# 	neigh.append(Vertex(v.x+dx, v.y+dy, v.dist+1))
	# return neigh

# visited: list[Vertex] = []

# def isVisited(toCheck: Vertex):
# 	for vertex in visited:
# 		if vertex.x == toCheck.x and vertex.y == vertex.y: return True
# 	return False

# def bfs(start: Vertex):
# 	global visited
# 	visited.append(start)
# 	queue = [start]

# 	while queue:
# 		current = queue.pop(0)
# 		neighbors = current.findNeighbors()
# 		print(len(queue), len(visited), len(neighbors))
# 		for neighbor in neighbors:
# 			if not neighbor.visited:
# 				visited.append(neighbor)
# 				queue.append(neighbor)

# bfs(Vertex(1, 1, 0))

# longest = 0
# for v in visited:
# 	if v.dist > longest: longest = v.dist
# print(longest)

# for v in visited:
# 	if v.visited:
# 		data[v.y][v.x] = "."

# output: list[str] = []
# for row in data:
# 	output.append(" ".join(row))

# with open("ar2.out", "w+") as file:
# 	file.write("\n".join(output))


with open("ar2.in", "r") as file:
	data = [[y for y in x] for x in file.read().split("\n")]

def getNeighbors(x: int, y: int) -> list[list[int]]:
	neigh: list[list[int]] = []
	for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		if x+dx > len(data[0]) or x+dx < 0: continue
		if y+dy > len(data) or y+dy < 0: continue
		value = data[x+dx][y+dy]
		if value != " ": continue
		neigh.append([x+dx, y+dy])
	return neigh


def bfs(x: int, y: int):
	queue = [[x, y]]
	visited = [[False for i in range(len(data))]
				for j in range(len(data[0]))]
	longestDist = 0
	while queue:
		current = queue.pop(0)
		neighbors = getNeighbors(current[0], current[1])
		data[current[0]][current[1]] = str(longestDist)
		longestDist += 1
		for neighbor in neighbors:
			if visited[neighbor[0]][neighbor[1]]: continue
			queue.append(neighbor)
			visited[neighbor[0]][neighbor[1]] = True
	return longestDist
print(bfs(1, 1))

with open("ar2.out", "w+") as file:
	file.write("\n".join([" ".join(["{:3s}".format(item) for item in row]) for row in data]))