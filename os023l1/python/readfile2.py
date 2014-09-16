#!/usr/bin/python
#Open a file
fo=open("foo.txt","r")
while True:
	
	str=fo.read(1)
	if str == '':
		break
	else:
		print "Read String is : ",str
		print "Position       : ",fo.tell()
fo.close()
fo=open("foo.txt","r")
str=fo.read()
print ("len : ",len(str))
