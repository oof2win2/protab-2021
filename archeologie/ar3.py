from heapq import *

wall_strength = 10

# shortest path is infinity so shorter paths exist
shortest_path = float("inf")

edges = []

class Node:
	def __init__(this, x: int, y: int, value: str):
		this.x = x
		this.y = y
		this.value = value
	def getEdges(this):
		global edges
		toReturn = []
		for edge in edges:
			if edge.start == this or edge.target == this:
				toReturn.append(edge)
		return toReturn

class Edge:
	def __init__(this, x: int, y: int, sv: str, tx: int, ty: int, ev: str, dist: int):
		# x, y is current position. tx, ty is target position. dist is distance to position
		this.start = Node(x, y, sv)
		this.target = Node(tx, ty, ev)
		this.dist = dist

visited: set[Node] = {}

def prepareGrid(grid: list[list[str]]) -> list[Edge]:
	edges: list[Edge] = []
	for y, row in enumerate(grid):
		for x, sv in enumerate(row):
			for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				if x+dx > len(grid[0])-1 or x+dx < 0: continue
				if y+dy > len(grid)-1 or y+dy < 0: continue
				print(y+dy, x+dx, len(grid[0]), len(grid))

				ev = grid[y+dy][x+dx]
				dist = 1 if sv == " " and ev == " " else wall_strength
				edges.append(Edge(x, y, sv, x+dx, y+dy, ev, dist))
	return edges

# TODO: do djikstra
# def Djikstra(nodes: list[list[Node]]):
# 	node = nodes[0][0]
# 	node.getEdges()
with open("ar3.in", "r") as file:
	grid = prepareGrid([[y for y in x] for x in file.read().split("\n")])
print(len(grid))