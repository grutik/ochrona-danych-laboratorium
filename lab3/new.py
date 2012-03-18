#!/usr/bin/python
import sys
import time

from Crypto.Cipher import ARC4
cipher = ARC4.new("key")
encrypted = cipher.encrypt("Top secret")
