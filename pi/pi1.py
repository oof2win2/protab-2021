with open("pi1000000.txt", "r") as file:
	pi = file.read()
with open("pi1.in", "r") as file:
	data = [int(x) for x in file.read().split(" ")]

redirected = [int(pi[x]) for x in data]
redirected2 = [int(pi[x]) for x in redirected]
print(sum(redirected), sum(redirected2), pi[sum(redirected)])
print(redirected, redirected2)

searched = [pi.find(str(x)) for x in data]
print([chr(65 + x % 26) for x in searched])