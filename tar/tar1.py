import tarfile
import os
import shutil

untars = 0
tars: list[str] = ["heslo.tar.gz"]
shutil.rmtree("./tar1")
os.mkdir("./tar1")
shutil.copyfile(tars[0], f"./tar1/{tars[0]}")


while True:
	# Place the heslo.tar.gz into the ./tar1/ folder
	if not tars: break
	tarName = tars.pop(0)
	tar = tarfile.open(f"./tar1/{tarName}")
	os.remove(f"./tar1/{tarName}")
	tar.extractall("tar1")
	dir = os.listdir("./tar1")
	for file in dir:
		if file.endswith(".tar.gz") and file not in tars:
			tars.append(file)
	untars += 1
	print(f"untarred {untars} times")
print("done")