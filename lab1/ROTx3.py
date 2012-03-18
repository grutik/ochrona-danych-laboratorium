#!/usr/bin/python
import string
import sys
#table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

n = 13
counter = 0
predict = 4
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
tekst = fileinput.input().rstrip()

while(counter < predict):
	for char in tekst:
		if(char == " "):
			sys.stdout.write(" ")
			temp += " "
			continue;	
		sys.stdout.write(table2[(std[char]+n)%26])
		temp += table2[(std[char]+n)%26]
	sys.stdout.write("\n")
	tekst = temp
	temp = ""
	counter = counter + 1

