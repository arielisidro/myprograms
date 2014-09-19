#!/usr/bin/python
# Open a file

fo = open("foo.txt", "r")

nlines = 0

while True:

    line = fo.readline()

    if line == '':
        break
    nlines += 1
    print "Read String is : ", line
    print "Position       : ", fo.tell()
    print "Number of lines: ", nlines

fo.close()
