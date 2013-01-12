#!/usr/bin/env python
import sys

print open(sys.argv[0]).read()

class rude:
    def burp(self):
        print 'pardon'

jerk=rude()

burp=getattr(jerk, 'burp') #must come from jerk, and not rude
burp() #or else this won't work

badBurp=getattr(rude, 'burp') #you can call it from the module
try:
    badBurp()
except TypeError as e:
    #but then you will end up here if you call it
    print 'fail:', e 

#last line of the file :)
