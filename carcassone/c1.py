from __future__ import annotations
import math

def common(a: list, b: list):
	return [ia for ia in a if ia in b]

class Tile:
	id = 0
	visited: list[int] = []
	def __init__(this, grid: list[str], value: int):
		this.id = Tile.id
		this.grid = grid
		this.value = value
		this.neighbors: list[Tile] = []
		this.visited = False
		Tile.id += 1
	
	def flipX(this) -> None:
		this.grid.reverse()
	
	def flipY(this) -> None:
		this.grid = [line[::-1] for line in this.grid]
	
	def rotate(this) -> None:
		this.grid = ["".join(list(reversed(x))) for x in zip(*this.grid)]
	
	def canRight(this, tile: Tile) -> bool:
		for y, line in enumerate(tile.grid):
			print(this.value, tile.value)
			if this.grid[y][-1] != line[0]:
				return False
		return True
	
	def canBottom(this, tile: Tile):
		return tile.grid[0] == this.grid[-1]

tiles: list[Tile] = []


with open("/Users/oof2win2/git/protab/carcassone/c1.in", "r") as file:
	data = [tile.split("\n") for tile in file.read().split("\n\n")]
	numTiles = len(data)
	maxLineLen = int(math.sqrt(numTiles))

	for tile in data:
		value = int(tile.pop(0).split(" ")[1])
		tile.pop(0) # remove the ---- line
		t = Tile(tile, value)
		tiles.append(t)

finalGrid: list[list[Tile]] = [[None for x in range(maxLineLen)] for y in range(maxLineLen)]

# def search():
# 	start: Tile = None
# 	canBeStartRight: list[Tile] = []
# 	canBeStartBottom: list[Tile] = []
# 	for tile in tiles:
# 		for compare in tiles:
# 			if tile == compare: continue

# 			if tile.canRight(compare):
# 				canBeStartRight.append(tile)
# 			if tile.canBottom(compare):
# 				canBeStartBottom.append(tile)
# 	print([x.value for x in canBeStartBottom], [x.value for x in canBeStartRight])
# 	start = common(canBeStartRight, canBeStartBottom)[0]
# 	print(start, start.value)
# search()

finalGrid[0][0] = tiles[0]

# TODO: fix this and make tile.visited False under some unknown conditions
def placeTiles(x: int, y: int):
	global tiles
	origin = finalGrid[y][x]
	for tile in tiles:
		if tile == origin: continue
		if tile.visited: continue

		print(origin.value, tile.value)

		for _ in range(2):
			for _ in range(2):
				for _ in range(4):
					if x+1 < len(finalGrid[0]) and origin.canRight(tile):
						print(y, x+1)
						finalGrid[y][x+1] = tile
						a = placeTiles(x+1, y)
						if a:
							tile.visited = True
							return True
					if y+1 < len(finalGrid) and origin.canBottom(tile):
						print(y+1, x)
						finalGrid[y+1][x] = tile
						a = placeTiles(x, y+1)
						if a:
							tile.visited = True
							return True
					tile.rotate()
				tile.flipX()
			tile.flipY()

def printGrid():
	print([[x.value for x in row if x] for row in finalGrid])

def run():
	returned = False
	x, y = 0, 0
	for row in finalGrid:
		for tile in row:
			print(tile)
	for tile in tiles:
		if returned:
			print("broke")
			break
		finalGrid[y][x] = tile
		returned = placeTiles(x, y)
	

	with open("c1.out", "w+") as file:
		file.write("\n".join([" ".join(["{:3s}".format(str(tile.value)) for tile in row]) for row in finalGrid]))
	for row in finalGrid:
		for tile in row:
			print(tile)
			if tile: print(tile.value)

run()