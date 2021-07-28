output = """
from constraint import *
problem = Problem()

"""

letters = []

constraints = """

problem.addConstraint(AllDifferentConstraint())

"""

with open("al2.in", "r") as file:
	input = file.read().split("\n")
length = input.pop(0)
output += f"problem.addVariables([chr(64+x) for x in range(1, {length})], range(1, {length}))"

for line in input:
	line = line.split()
	print(line)
	if line[3] == "liché":
		letters.append(line[0])
		constraints += f"problem.addConstraint(lambda {line[0]}: {line[0]} % 2 == 1, [\"{line[0]}\"])"
	elif line[3] == "sudé":
		letters.append(line[0])
		constraints += f"problem.addConstraint(lambda {line[0]}: {line[0]} % 2 == 0, [\"{line[0]}\"])"
	elif line[3] in ["pozic", "pozice", "pozici"]:
		letters.append(line[0])
		letters.append(line[-1])
		constraints += f"problem.addConstraint(lambda {line[0]}, {line[-1]}: abs({line[0]} - {line[-1]}) == {line[2]}, [\"{line[0]}\", \"{line[-1]}\"])"
	elif line[2] == "nalevo":
		letters.append(line[0])
		letters.append(line[-1])
		constraints += f"problem.addConstraint(lambda {line[0]}, {line[-1]}: {line[0]} < {line[-1]}, [\"{line[0]}\", \"{line[-1]}\"])"
	elif line[2] == "napravo":
		letters.append(line[0])
		letters.append(line[-1])
		constraints += f"problem.addConstraint(lambda {line[0]}, {line[-1]}: {line[0]} > {line[-1]}, [\"{line[0]}\", \"{line[-1]}\"])"
	constraints += "\n"

constraints += """
sol = problem.getSolution()
print(sol)

res = ""
while len(sol):
	lowest = min(zip(sol.values(), sol.keys()))
	res += f"{lowest[1]} "
	sol.pop(lowest[1])
print(res)
"""

with open ("al2out.py", "w+") as file:
	file.write(output+constraints)

# with open("al2.in") as file:
#     lines = file.readlines()
# code = ""

# for line in lines:
#     line = line.split()
#     if line[3] == "liché":
#         code += f"problem.addConstraint(lambda {line[0]}: {line[0]} % 2 == 1, [\"{line[0]}\"])\n"
#     elif line[3] == "sudé":
#         code += f"problem.addConstraint(lambda {line[0]}: {line[0]} % 2 == 0, [\"{line[0]}\"])\n"
#     elif line[3] in ["pozic", "pozice", "pozici"]:
#         code += f"problem.addConstraint(lambda {line[0]}, {line[5]}: abs({line[0]} - {line[5]}) == {line[2]}, [\"{line[0]}\", \"{line[5]}\"])\n"
#     elif line[2] == "napravo":
#         code += f"problem.addConstraint(lambda {line[0]}, {line[4]}: {line[0]} > {line[4]}, [\"{line[0]}\", \"{line[4]}\"])\n"
#     elif line[2] == "nalevo":
#         code += f"problem.addConstraint(lambda {line[0]}, {line[4]}: {line[0]} < {line[4]}, [\"{line[0]}\", \"{line[4]}\"])\n"

# print(code)