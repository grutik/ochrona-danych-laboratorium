#!/usr/bin/python
import sys, re, string
import math

def histogram(data):
	total = 0.0;
	stat = {}
	for line in data:
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

	return prawdopodob

def entropy(data):
	prawdopodob = histogram(data)
	entropy = 0
	for znak in prawdopodob:
		if(prawdopodob[znak] > 0):
			entropy = entropy + prawdopodob[znak] * math.log(prawdopodob[znak],2.0)

	return entropy*(-1)

print entropy("oifdaspoijdgfoiajsdoigjasoijdgoiajsdg")
