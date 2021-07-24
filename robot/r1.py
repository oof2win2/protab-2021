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

def getNeighbours(x: int, y: int) -> list:
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

def run():
	while len(vertexes):
		vertex = vertexes.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			point = data[vertex[0]][vertex[1]]

			if point.isalpha() and point.islower():
				unlocked.append(point)
				removeFromData(point)
			
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