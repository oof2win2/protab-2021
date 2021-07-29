import tarfile
import shutil
import os

untars = 0
tars: list[str] = ["heslo_znovu.tar.gz"]
shutil.rmtree("./tar2")
os.mkdir("./tar2")
shutil.copyfile(tars[0], f"./tar2/{tars[0]}")


while True:
	# Place the heslo.tar.gz into the ./tar1/ folder
	if not tars: break
	tarName = tars.pop(0)
	tar = tarfile.open(f"./tar2/{tarName}")
	os.remove(f"./tar2/{tarName}")
	tar.extractall("tar2")
	dir = os.listdir("./tar2")
	for file in dir:
		if file.endswith(".tar.gz") and file not in tars:
			tars.append(file)
	untars += 1
	print(f"untarred {untars} times")
print("done")