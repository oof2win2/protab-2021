with open("ar2.in", "r") as file:
	data = [[y for y in x] for x in file.read().split("\n")]

def getNeighbors(x: int, y: int, dist: int):
	neigh: list[list[int]] = []
	for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		if x+dx > len(data[0]) or x+dx < 0: continue
		if y+dy > len(data) or y+dy < 0: continue
		value = data[x+dx][y+dy]
		if value != " ": continue
		# data[x+dx][y+dy] = str(dist)
		neigh.append([x+dx, y+dy])
	return neigh

def bfs(x: int, y: int):
	visited = [[False for i in range(len(data))]
				for j in range(len(data[0]))]
	queue = [[x, y, 0]]

	longestDist = 0
	l = 0
	while queue:
		print(len(queue))
		current = queue[0]
		data[current[0]][current[1]] = str(current[2])
		for vertex in queue:
			if vertex[2] != longestDist: continue
			neighbors = getNeighbors(vertex[0], vertex[1], longestDist+1)
			for neighbor in neighbors:
				if visited[neighbor[0]][neighbor[1]]: continue
				queue.append([*neighbor, longestDist+1])
				data[neighbor[0]][neighbor[1]] = str(longestDist)
				l = longestDist
				visited[neighbor[0]][neighbor[1]] = True
		queue.pop(0)
		longestDist += 1
	return l
print(bfs(1, 1))

with open("ar2.out", "w+") as file:
	file.write("\n".join([" ".join(["{:3s}".format(item) for item in row]) for row in data]))