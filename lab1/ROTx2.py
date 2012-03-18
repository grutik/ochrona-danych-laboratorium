#!/usr/bin/python
import string
import sys
#table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

n = 13;
print "n: ", n
alphabet = "abcdefghijklmnopqrstuvwxyz"

#print slownik
#print std

import fileinput
for line in fileinput.input():
        line = line.rstrip()
	for char in line:
		sys.stdout.write(ord(char))
	sys.stdout.write("\n")
