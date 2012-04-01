#!/usr/bin/python
import sys
import random
import math
from Crypto.Cipher import DES,AES
import time
import hashlib

## otwarcie pliku
plain = open(sys.argv[1])
haslo = sys.argv[2]

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
##############################################
aes = AES.new(key,AES.MODE_CBC)
cryptogram  = aes.decrypt(new)
print cryptogram

