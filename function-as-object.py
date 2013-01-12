#!/usr/bin/env python
import sys

f=open(sys.argv[0])
print f.read()

class rude:
    def burp(self):
        print 'pardon'

jerk=rude()

burp=getattr(jerk, 'burp')

burp()

#last line of the file :)
