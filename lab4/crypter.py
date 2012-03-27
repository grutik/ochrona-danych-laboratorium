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

## Losowa sol:
sol = ""
for s in range(8):
	sol += str(random.randint(0,9))
print "sol:"
print sol
password = hashlib.sha224(haslo).hexdigest()
for i in range(1000):
	password = hashlib.sha224(password+str(sol)).hexdigest()
print "pass:"
print password

## Okrojenie klucza:
key = ""
k = 0
for i in password:
	key += str(i) 
	if k == 15:
		break
	k = k +1

print "key:"
print key

## Wczytanie pliku do zmiennej:
inputFile = ""
for line in plain.readlines():
   for char in line:
      inputFile += char


##############################################
aes = AES.new(key,AES.MODE_CBC)
cryptogram  = aes.encrypt(inputFile)

file = open(sys.argv[3], 'w')
file.write(sol)
file.write(cryptogram)	
