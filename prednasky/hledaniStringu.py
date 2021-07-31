jehla = "baobab"
seno = "baobabbab"
zpet = [0] * len(jehla)

def krok(s: int, p):
	while s != 0 and p != jehla[s]:
		s = zpet[s-1]
	if jehla[s] == p:
		s += 1
	return s

s = 0
for i in range(1, len(jehla)):
	s = krok(s, jehla[i])
	zpet[i] = s
print(s, zpet)

s = 0
for p in seno:
	s = krok(s, p)
	if s == len(jehla):
		print("found 1")