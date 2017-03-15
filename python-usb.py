#import things :)
from time import sleep
import os
from os.path import exists
from shutil import copy2

f=open('path.txt','r') #reading from path.txt
list = f.readlines()
path = list[0].rstrip() #removes \n from string
dst = list[1].rstrip()
f.close()
while (True):
    sleep(5)
    if exists(path): # loking for src path 
        for path , dirs ,files in os.walk(path): # searchs the src recursively
            for name in files :
                if name.endswith((".pdf",".docx")):
                    print(name)
                    copy2(os.path.join(path,name),dst)
        print(30*"---","\n Done.")
        exit()
