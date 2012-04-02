#!/usr/bin/python
import sys
import random
import math
from Crypto.Cipher import DES,AES
import time
import hashlib
import time

import sys, re, string
import math

limit = 0
pdfFormat = open('pdf.format','rb').read()
jpgFormat = open('jpg.format','rb').read()

def histogram(data):
	total = 0.0;
	stat = {}
	limit = 200
	for line in data:
		if total == limit:
			break
		line = re.sub(r'\s', '', line)
		for znak in line:
			if znak in stat:
				stat[znak] += 1
			else:
				stat[znak] = 0
			total = total + 1
			if total == limit:
				break

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

## otwarcie pliku
plain = open(sys.argv[1])
inputFile = ""
for line in plain.readlines():
	for char in line:
		inputFile += char
	
sol = ""
ss = 0
for s in inputFile:
	sol += s
	ss = ss + 1
	if ss == 8:
		break
#print "Sol:"
#print sol

#print "inputFile:"
#print inputFile
new = ""
i = 0
for f in inputFile:
	if i < 8:
		i = i +1
		continue
	else:
		new += f
	i = i +1

reszta = len(new)%16
#print "Reszta:"
#print reszta
for i in range(reszta):
	new += " "


#print "new:"
#print new

found = 0
#generowanie hasla
chars = string.ascii_letters
for a in chars:
	if found == 1:
		break
	for b in chars:
		if found == 1:
			break
		for c in chars:
			if found == 1:
				break
			haslo = a+b+c

			password = hashlib.sha224(haslo).hexdigest()
			for i in range(1000):
				password = hashlib.sha224(password+str(sol)).hexdigest()

			key = ""
			k = 0
			for i in password:
				key += str(i) 
				if k == 15:
					break
				k = k +1
			#print "Key:"
			#print key
			#print ""

#############################################
			aes = AES.new(key,AES.MODE_CBC)
			cryptogram  = aes.decrypt(new)

			header = cryptogram[0:30]
#			print header
			#entropia = str(entropy(naglowek))
			
			if header == pdfFormat or header == jpgFormat:
				found = 1
				file = open(sys.argv[2], 'wb')
				for item in cryptogram:
					file.write(''.join(item))	
				break
