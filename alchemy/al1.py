from constraint import *

problem = Problem()

problem.addVariables(["A", "B", "C", "D", "E", "F", "G", "H"], range(1, 9))

problem.addConstraint(AllDifferentConstraint())

#	F je na sudé pozici
#	H je nalevo od D
#	A je 5 pozic od E
#	H je napravo od G
#	G je 3 pozice od C
#	F je napravo od C
#	D je na sudé pozici
#	C je na sudé pozici
#	E je nalevo od H
#	F je napravo od D
#	D je 2 pozice od C
#	B je nalevo od H

problem.addConstraint(lambda f: f % 2 == 0, ["F"])
problem.addConstraint(lambda h, d: h < d, ["H", "D"])
problem.addConstraint(lambda a, e: abs(a - e) == 5, ["A", "E"])
problem.addConstraint(lambda h, g: h > g, ["H", "G"])
problem.addConstraint(lambda g, c: abs(g - c) == 3, ["G", "C"])
problem.addConstraint(lambda f, c: f > c, ["F", "C"])
problem.addConstraint(lambda d: d % 2 == 0, ["D"])
problem.addConstraint(lambda c: c % 2 == 0, ["C"])
problem.addConstraint(lambda e, h: e < h, ["E", "H"])
problem.addConstraint(lambda d, c: abs(d - c) == 2, ["D", "C"])
problem.addConstraint(lambda b, h: b < h, ["B", "H"])

print(problem.getSolution())