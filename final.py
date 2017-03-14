#.......Jäger.......

import os
from os.path import exists
from platform import system as cos
from shutil import copy2 

while (True):
	if (cos()== "Linux"):
		if exists("/run/media/abtin"): #for ubuntu --> /media/abtin
			for root ,dirs , files in os.walk("/run/media/abtin"):
				for name in files :
					if name.endswith((".pdf",".docx")):
						print(name)
						copy2(os.path.join(root,name),"/home/abtin/test")
			print(30*"---","\n Done.")
			exit()

	if (cos()== "Windows"):
		if exists("f:"):
			path = "f:\\"
			for path , dirs ,files in os.walk(path):
				for name in files :
					if name.endswith((".pdf",".docx")):
						print(name)
						copy2(os.path.join(path,name),"d:\\test")
			print(30*"---","\n Done.")
			exit()
