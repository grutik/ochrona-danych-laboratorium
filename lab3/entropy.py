#!/usr/bin/python
import sys
import math

#licze logarytm o podstawie 2 z calego mozliwego alfabetu znakow, a nastepnie mnoze wynik przez liczbe znakow w hasle
#s - alfabet mozliwych znakow, leng - dlugosc hasla
def getEntropy(alphabet, leng):
   
   log = math.log(len(alphabet),2)

   print "passLength: %d" %leng
   print "passEntropy: %f" %(leng*log)
   return leng*log
