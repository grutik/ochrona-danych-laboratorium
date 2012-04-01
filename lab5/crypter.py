#!/usr/bin/python
import sys
import random
import math
from Crypto.Cipher import DES,AES
import time
import hashlib
########## Otworzenie pliku ############
plain = open(sys.argv[1])
haslo = sys.argv[2]
random.seed(time.time())

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

## Losowa sol:
sol = ""
for s in range(8):
	sol += str(random.randint(0,9))
#print "sol:"
#print sol
password = hashlib.sha224(haslo).hexdigest()
for i in range(1000):
	password = hashlib.sha224(password+str(sol)).hexdigest()
#print "pass:"
#print password

## Okrojenie klucza:
key = ""
k = 0
for i in password:
	key += str(i) 
	if k == 15:
		break
	k = k +1

#print "key:"
#print key

## Wczytanie pliku do zmiennej:
inputFile = ""
for line in plain.readlines():
   for char in line:
      inputFile += char

while(len(inputFile)%16 <> 0):
	inputFile += " "
#print "Reszta:"
#print len(inputFile)%16

#print inputFile
##############################################
#print "N:"
#print n

aes = AES.new(key,AES.MODE_CBC)
cryptogram  = aes.encrypt(inputFile)
file = open(sys.argv[3], 'w')
file.write(sol)
file.write(cryptogram)	


