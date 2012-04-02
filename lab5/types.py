#!/usr/bin/python
import sys

plain = open(sys.argv[1],'rb').read()
open(sys.argv[2],'wb').write(plain[0:30])	
