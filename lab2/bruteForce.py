#!/usr/bin/python
import crypt
import sys
import string
import time


baza = open(sys.argv[1])
chars = string.ascii_letters
print len(chars)

for line in baza:
	#print line
	parts = line.split(":")
	parts[0] = parts[0].rstrip()
	parts[1] = parts[1].rstrip()


	t1 = time.time()
	for a in chars:
		for b in chars:
			for c in chars:
				trial = a+b+c
				newHash = crypt.crypt( trial, parts[1])
				if newHash == parts[1]:
					print parts[0] + " : " + trial
					t2 = time.time()
					diff = t2 - t1
					print "czas: "+str(diff)+"s"
					print ""
					break
