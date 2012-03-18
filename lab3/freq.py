#!/usr/bin/python
import sys, re, string
import math

plain = open(sys.argv[1])
inputFile = ""

total = 0.0;
stat = {}
for line in plain:
        line = re.sub(r'\s', '', line)
        for znak in line:
                if znak in stat:
                        stat[znak] += 1
                else:
                        stat[znak] = 0
		total = total + 1

prawdopodob = {}
for znak in stat:
	prawdopodob[znak] = stat[znak]/total

#print prawdopodob

#entropia
entropy = 0
for znak in prawdopodob:
	if(prawdopodob[znak] > 0):
		entropy = entropy + prawdopodob[znak] * math.log(prawdopodob[znak],2.0)


print "Entropia pliku:" 
print entropy*-1
