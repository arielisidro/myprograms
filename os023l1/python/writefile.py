#!/usr/bin/python
#Open a file
fo = open("foo.txt","wb")
print "Name of the file:",fo.name
fo.write("Python is a great language.\nYeah its great!!!\n")

#close the file
fo.close()
