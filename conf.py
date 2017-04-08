path = input("Wlc to conf file :\n\nEnter path(src):") #get src and dst from user
dst = input("Enter dst:")
print ("path(src)= %s\ndst = %s \n" %(path,dst))
yn = input ("save changes?(y/n)  ") #asks for writing
if (yn =='y'or yn =='Y'):
	f=open('path.txt','w') #writing to path.txt 
	f.writelines([path,'\n',dst])
	f.close()
else:
	print("Abort.")   
