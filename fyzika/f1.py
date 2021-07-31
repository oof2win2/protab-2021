from __future__ import annotations
## TODO: stuff

class Moon:
	def __init__(this, x: int, y: int, z: int, sx: int, sy: int, sz: int):
		this.x = x
		this.y = y
		this.z = z

		this.sx = sx
		this.sy = sy
		this.sz = sz
	def moveGravity(this, relativeMoon: Moon):
		"""
		move moons relative to each other with their positions
		"""
		if this.x - relativeMoon.x > 0:
			this.sx -= 1
			relativeMoon.sx += 1
		elif this.x - relativeMoon.x < 0:
			this.sx += 1
			relativeMoon.sx -= 1
		
		if this.y - relativeMoon.y > 0:
			this.sy -= 1
			relativeMoon.sy += 1
		elif this.y - relativeMoon.y < 0:
			this.sy += 1
			relativeMoon.sy -= 1
		
		if this.z - relativeMoon.z > 0:
			this.sz -= 1
			relativeMoon.sz += 1
		elif this.z - relativeMoon.z < 0:
			this.sz += 1
			relativeMoon.sz -= 1

	def moveSpeed(this):
		"""
		move moon with its own speed
		"""
		this.x += this.sx
		this.y += this.sy
		this.z += this.sz

	def __eq__(this, o: Moon):
		if this.x != o.x: return False
		if this.y != o.y: return False
		if this.z != o.z: return False

		if this.sx != o.sx: return False
		if this.sy != o.sy: return False
		if this.sz != o.sz: return False

		return True
	def __ne__(this, o: Moon):
		if this.x == o.x: return False
		if this.y == o.y: return False
		if this.z == o.z: return False

		if this.sx == o.sx: return False
		if this.sy == o.sy: return False
		if this.sz == o.sz: return False

		return True



startMoonData = [
	[-13, 14, -7, 0, 0, 0],
	[-18, 9, 0, 0, 0, 0],
	[0, -3, -3, 0, 0, 0],
	[-15, 3, -13, 0, 0, 0],
]
startMoons = [Moon(*a) for a in startMoonData]

moons = [Moon(*a) for a in startMoonData]

def krok():
	movedMoons: list[list[int]] = []
	for moon in moons:
		for toMove in moons:
			if moon == toMove: continue
			if [moon, toMove] in movedMoons or [toMove, moon] in movedMoons: continue
			movedMoons.append([moon, toMove])
			moon.moveGravity(toMove)
	for moon in moons:
		moon.moveSpeed()

def checkOriginal() -> bool:
	for i, moon in enumerate(moons):
		if moon == startMoons[i]: continue
		return False
	return True

def slozekRychlosti():
	total = 1
	for moon in moons:
		total *= moon.sx
		total *= moon.sy
		total *= moon.sz
	return total

for moon in moons:
	print("{:3d} {:3d} {:3d} {:3d} {:3d} {:3d}".format(moon.x, moon.y, moon.z, moon.sx, moon.sy, moon.sz))



for i in range(10000):
	krok()
print("\n")

for moon in moons:
	print("{:3d} {:3d} {:3d} {:3d} {:3d} {:3d}".format(moon.x, moon.y, moon.z, moon.sx, moon.sy, moon.sz))
print("\n")
print(slozekRychlosti() * slozekRychlosti())



stepsToReturn = 0

# while True:
# 	stepsToReturn += 1
# 	krok()
# 	if checkOriginal(): break
# for moon in moons:
# 	print("{:3d} {:3d} {:3d} {:3d} {:3d} {:3d}".format(moon.x, moon.y, moon.z, moon.sx, moon.sy, moon.sz))
# print(stepsToReturn)