#!/usr/bin/python
import string
table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")
import fileinput

for line in fileinput.input():
        line = line.rstrip()
        print string.translate(line, table)
