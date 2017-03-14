path = input("Wlc to conf file :\n\nEnter path(src):")
dst = input("Enter dst:")
print ("path(src)= %s\ndst = %s \n" %(path,dst))
yn = input ("save changes?(y/n)  ")
if (yn =='y'or yn =='Y'):
	f=open('path.txt','w')
	f.writelines([path,'\n',dst])
	f.close()
else:
	print("Abort.")   