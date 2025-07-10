import os
import shutil
folderc = os.path.expanduser("~/Desktop/syf")
folderd = os.path.expanduser("~/Desktop/gold")
	for filename in os.listdir(folderc):
	filep = os.path.join(folderc, filename)
	if filename.lower().startswith("w") and os.path.isfile(filep) :
		newp = os.path.join(folderd, filename)
		shutil.copy(filep, newp)
		print(f"copied: {filename}")
