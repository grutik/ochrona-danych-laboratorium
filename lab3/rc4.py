#!/usr/bin/python
import sys
import time

def rc4crypt(plaintext, key):
	s = range(256)
	#print s
	j = 0
	for i in range(256):
		j = (j + s[i] + ord(key[i%len(key)]))%256
		s[i], s[j] = s[j], s[i]

	i = 0
	j = 0	

	stream = []
	for char in plaintext:
	      i = (i + 1) % 256
	      j = (j + s[i]) % 256
	      s[i], s[j] = s[j], s[i]
	      stream.append(s[(s[i] + s[j]) % 256]);

	return stream

def xor(plaintext, strumien):
	result = []
	i = 0
	for char in plaintext:
		result.append(chr(ord(char) ^ strumien[i]))
		i += 1
	return result

plain = open(sys.argv[1])
#print plain
key = sys.argv[2]
#print key
inputFile = ""

for line in plain.readlines():
   for char in line:
      inputFile += char

t1 = time.time()
newStream =  rc4crypt(inputFile, key)
t2 = time.time()
cryptogram = xor(inputFile,newStream)

file = open(sys.argv[3], 'wb')
for item in cryptogram:
   file.write(''.join(item))	


diff = t2 - t1
print diff


