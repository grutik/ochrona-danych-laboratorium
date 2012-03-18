#!/usr/bin/python
import crypt
import sys
import string
import time




def trivial_hash(dane):
	hash = 0
	for line in dane:
		for znak in line:
			hash += ord(znak)
	return hash % 999

p1 = open("p1.html")
p2 = open("p2.html")


print trivial_hash(p1)
print trivial_hash(p2)

