#!/usr/bin/python
#Open a file
fo=open("foo.txt","r")
nlines=0
while True:
	str=fo.readline()

	if str == '':
		break
	nlines += 1
	print "Read String is : ",str
	print "Position       : ",fo.tell()
	print "Number of lines: ",nlines

fo.close()
