from __future__ import annotations
import heapq

with open("ar3.in", "r") as file:
	data = [[y for y in x] for x in file.read().split("\n")]

# some constants
startx, starty = 1, 1
goalx, goaly = 499, 499
wall_strength = 11

edges: list[Edge] = []

class Node:
	def __init__(this, x: int, y: int, value: str, dist: float = float("inf")):
		this.x = x
		this.y = y
		this.value = value
		this.dist = dist
		this.visited = False
		this.edges = []
	
	def __eq__(self, o: Node):
		return self.dist == o.dist
	def __ne__(self, o: Node):
		return self.dist != o.dist
	def __lt__(self, o: Node):
		return self.dist < o.dist
	def __gt__(self, o: Node):
		return self.dist > o.dist
	

nodes = [[Node(x, y, space) for x, space in enumerate(row)]
			for y, row in enumerate(data)]

nodes[starty][startx].dist = 0

class Edge:
	def __init__(this, start: Node, target: Node, dist: float = float("inf")):
		# x, y is current position. tx, ty is target position. dist is distance to position
		this.start = start
		this.target = target
		this.dist = dist

# print(len(nodes), len(nodes[0]), nodes[500])

def getNeighbors(node: Node) -> list[Node]:
	neighbors: list[Node] = []
	for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		if node.x+dx > len(nodes[0])-1 or node.x+dx < 0: continue
		if node.y+dy > len(nodes)-1 or node.y+dy < 0: continue
		# print(node.y+dy, node.x+dx)
		neighbor = nodes[node.y+dy][node.x+dx]
		neighbors.append(neighbor)
	return neighbors


for row in nodes:
	for node in row:
		neighbors = getNeighbors(node)
		for neighbor in neighbors:
			dist = 1 if neighbor.value == " " else wall_strength
			edge = Edge(node, neighbor, dist)
			node.edges.append(edge)
			neighbor.edges.append(edge)
del neighbors

def dijkstra():
	queue = [nodes[starty][startx]]
	output = [[0.0 for space in row] for row in nodes]
	heapq.heapify(queue)

	while queue:
		node = heapq.heappop(queue)
		for edge in node.edges:
			neighbor = edge.target
			if neighbor.dist > (node.dist + edge.dist):
				neighbor.dist = node.dist + edge.dist
				output[neighbor.y][neighbor.x] = neighbor.dist
				if neighbor.visited: continue
				neighbor.visited = True
				heapq.heappush(queue, neighbor)
		
	print("done")
	print(output[goaly][goalx])
	with open("ar3.out", "w+") as file:
		file.write("\n".join([" ".join(["{:3s}".format(f"{node:.0f}") for node in row]) for row in output]))

# print(data[10][9], nodes[10][9], nodes[10][9].getEdges()[0].dist)

dijkstra()