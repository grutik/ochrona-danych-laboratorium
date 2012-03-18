#!/usr/bin/python
import crypt
import sys

baza = open("baza")

for line in baza:
	#print line
	parts = line.split(":")
	parts[0].rstrip()
	parts[1].rstrip()
	if parts[0] == sys.argv[1]:
		newHash = crypt.crypt(sys.argv[2],parts[1] )
		if newHash == parts[1].rstrip():
			print newHash
			print parts[1]
			print "Uzytkownik istnieje"
		

#if len(sys.argv) == 3:
#   print("%s:%s" % (sys.argv[1], crypt.crypt(sys.argv[2], sys.argv[2])))
