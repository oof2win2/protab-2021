import pulp

with open("p1data/p_i.in") as file:
	p_i = [int(x) for x in file.read().split(" ")]
with open("p1data/o_i.in") as file:
	o_i = [int(x) for x in file.read().split(" ")]
with open("p1data/c_ij.in") as file:
	p_ij = [[y for y in x.split(" ")] for x in file.read().split("\n")]
print(sum(p_i), sum(o_i))

model = pulp.LpProblem()

p_upece = pulp.LpVariable(name="p_upece", lowBound=0, cat="integer", upBound=sum(p_i))
p_proda = pulp.LpVariable(name="p_proda", lowBound=0, cat="integer", upBound=sum(o_i))
p_stoji = pulp.LpVariable(name="p_stoji", lowBound=0, cat="integer", upBound=sum(c_ij))

model += p_upece
model += p_proda
model += p_stoji

print(model.solve())

chonr ih vhbvr.pav r vprgcy .rmlnu.reabhiou, a vr vab.rjprm
hepxl je teqtlknat l tnlchu klmbxiklvaqejpi, a tl taqkldnlm 
heslo je tentokrat o trochu 