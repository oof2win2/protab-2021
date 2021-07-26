with open("ar1.in", "r") as file:
    data = [[y for y in x] for x in file.read().split("\n")]

def findNeighbors(x: int, y: int):
	data[y][x] = "."
	for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
		if data[y+dy][x+dx] == " ":
			data[y+dy][x+dx] = "."
			findNeighbors(x+dx, y+dy)

countAreas = 0
for y, row in enumerate(data):
	for x, space in enumerate(row):
		if space == " ":
			findNeighbors(x, y)
			countAreas += 1
# n = findNeighbors(2, 19)
# print(n)

# n = findNeighbors(2, 18)
print(countAreas)