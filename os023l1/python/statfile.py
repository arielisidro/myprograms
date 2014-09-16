#!/usr/bin/python

#open a file
fo = open("readfile.py","r")
print "Name of the file: ",fo.name
print "Close or not : ",fo.closed
print "Opening mode : ",fo.mode
print "Softspace flag:",fo.softspace

fo.close()

