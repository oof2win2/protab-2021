import time

with open("r1.in", "r") as file:
    data = [[y for y in x] for x in file.read().split("\n")]

roboyX = 0
robotY = 0
charPositions = []

for y, row in enumerate(data):
	for x, space in enumerate(row):
		if space == "@":
			roboyX, robotY = x, y
		if space.islower() and space.isalpha():
			charPositions.append([y, x])

vertexes = [[roboyX, robotY]]
visited = []
unlocked = []

def checkPoint(x: int, y: int) -> bool:
	if (y > len(data) or y < 0): return False
	if (x > len(data[0]) or x < 0): return False

	point = data[y][x]
	if point == "#": return False
	if point.isupper() and point.lower() not in unlocked: return False
	return True

def getNeighbours(x: int, y: int) -> list[list[int]]:
	neighbours = []
	if checkPoint(x, y+1): neighbours.append([x, y+1])
	if checkPoint(x, y-1): neighbours.append([x, y-1])
	if checkPoint(x+1, y): neighbours.append([x+1, y])
	if checkPoint(x-1, y): neighbours.append([x-1, y])
	return neighbours

def checkGoal() -> bool:
	for row in data:
		for space in row:
			if space.islower(): return False
	return True

def removeFromData(point: str):
	for y, row in enumerate(data):
		for x, space in enumerate(row):
			if space == point:
				data[y][x] = " "
			if space.lower() == point:
				data[y][x] = " "
def moveRobot(robPosX: int, robPosY: int):
	for y, row in enumerate(data):
		for x, space in enumerate(row):
			if space == "@":
				data[y][x] = " "
	data[robPosY][robPosX] = "@"

def findNeighborsForWall(point: str):
	for y, row in enumerate(data):
		for x, space in enumerate(row):
			if space == point.upper():
				return getNeighbours(x, y)
	return []

def run():
	while len(vertexes):
		vertex = vertexes.pop(0)
		if vertex not in visited:
			# time.sleep(0.05)
			visited.append(vertex)
			# print(vertex, data)
			point = data[vertex[1]][vertex[0]]
			data[vertex[1]][vertex[0]] = "."
			# print(vertexes)
			if point.isalpha() and point.islower():
				unlocked.append(point)
				nei = findNeighborsForWall(point)
				for n in nei:
					vertexes.append(n)
				removeFromData(point)
				# with open("r1.out", "w") as file:
				# 	file.write("\n".join(["".join(row) for row in data]))
				# time.sleep(2)
			
			neighbours = getNeighbours(vertex[0], vertex[1])
			for neighbour in neighbours:
				vertexes.append(neighbour)
			moveRobot(vertex[0], vertex[1])
			
			if checkGoal(): break
	
	print(len(visited))

run()

with open("r1.out", "w+") as file:
	for i, row in enumerate(data):
		data[i] = "".join(row)
	file.write("\n".join(data))

# import time

# class Vertex:
# 	def __init__(this, x: int, y: int, value: str):
# 		this.x = x
# 		this.y = y
# 		this.isKey = False
# 		this.isGate = False
# 		this.neighbors: list[Vertex] = []
# 		this.value = value

# 	def addNeighbor(this, neigbor):
# 		this.neighbors.append(neigbor)
# 		return


# class Grid:
# 	def __init__(this, grid: list[list[str]]):
# 		this.start: Vertex = None
# 		this.vertices: list[list[Vertex]] = []
# 		this.nextUp: list[Vertex] = []
# 		for y, row in enumerate(grid):
# 			rowList: list[Vertex] = []
# 			for x, space in enumerate(row):
# 				v = Vertex(x, y, space)
# 				if space == "@":
# 					this.start = v
# 				if space.isalpha() and space.islower():
# 					v.isKey = True
# 				if space.isalpha() and space.isupper():
# 					v.isGate = True
# 				rowList.append(v)
# 			this.vertices.append(rowList)
# 	def __moveRobot(this, x: int, y: int):
# 		for y, row in enumerate(this.vertices):
# 			for x, vertex in enumerate(row):
# 				if vertex.value == "@":
# 					vertex.value = " "
# 		this.vertices[y][x].value = "@"
# 		return
# 	def __removeGate(this, gate: str):
# 		for y, row in enumerate(this.vertices):
# 			for x, vertex in enumerate(row):
# 				if vertex.value.lower() == gate:
# 					vertex.value = " "
# 					vertex.isGate = False
# 					vertex.isKey = False
# 					this.vertices[y][x] = vertex
# 		return
# 	def __tryGetVertex(this, x: int, y: int) -> Vertex:
# 		v = this.vertices[y][x]
# 		if v.value == "#": return None
# 		if v.y != y or v.x != x: return None
# 		return v
# 	def __getNeighbors(this, vertex: Vertex) -> list[Vertex]:
# 		neighbors: list[Vertex] = [
# 		this.__tryGetVertex(vertex.x, vertex.y - 1),
# 		this.__tryGetVertex(vertex.x + 1, vertex.y),
# 		this.__tryGetVertex(vertex.x, vertex.y + 1),
# 		this.__tryGetVertex(vertex.x - 1, vertex.y),
# 		]
# 		for i, v in enumerate(neighbors):
# 			if v == None: neighbors.pop(i)
# 		return neighbors
# 	def checkWin(this) -> bool:
# 		for row in this.vertices:
# 			for vertex in row:
# 				if vertex.value.isalpha(): return False
# 		return True
# 	def bfs(this) -> int:
# 		while this.nextUp:
# 			vertex = this.nextUp.pop(0)
# 			neighbors = this.__getNeighbors(vertex)
# 			for neighbor in neighbors: this.nextUp.append(neighbor)
# 			if vertex.isKey:
# 				this.__removeGate(vertex.value)
# 				## TODO: remove from nextUp
# 				this.nextUp = this.nextUp.
# 				this.nextUp = [vertex for vertex in this.nextUp]
			
		

# with open("r1.in", "r") as file:
# 	mazeData = [[y for y in x] for x in file.read().split("\n")]

# maze = Grid(mazeData)
# print(maze.bfs())
			