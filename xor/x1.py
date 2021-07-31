with open("x1.in", "r") as file:
	data = file.read().split(", ")
sum = 0
while data:
	item = int(data.pop(0))
	if item == 15:
		print(sum)
		sum = 0
	sum = sum ^ item
print(sum)