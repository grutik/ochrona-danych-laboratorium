#!/usr/bin/python
import string
import sys
#table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

n = 13
counter = 0
predict = 1
print "n: ", n
table2 = "abcdefghijklmnopqrstuvwxyz"
slownik = {}
std = {}
for char in range(len(table2)):
	slownik[char] = table2[char]
	std[table2[char]] = char
#print slownik
#print std
temp = ""
import fileinput
for line in fileinput.input():
        line = line.rstrip()
	for char in line:
		if(char == " "):
			sys.stdout.write(" ")
			temp += " "
			continue;	
		sys.stdout.write(table2[(std[char]+n)%26])
		temp += table2[(std[char]+n)%26]
	sys.stdout.write("\n")
	counter = counter + 1

temp2 = ""

for char in temp:
	if(char == " "):
		sys.stdout.write(" ")
		temp2 += " "
		continue;	
	sys.stdout.write(table2[(std[char]+n)%26])
	temp2 += table2[(std[char]+n)%26]

sys.stdout.write("\n")

