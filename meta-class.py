#!/usr/bin/env python

import sys, hashlib

if len(sys.argv) < 2 or sys.argv[1] != '-q':
    with open(sys.argv[0]) as me:
        print me.read()

class Hasher(type):
    # maybe handy for versioning?
    def __new__(cls, name, bases, attrs):
        attrs['hash']=hashlib.sha1(name + str(bases) + str(attrs)).hexdigest()
        return type.__new__(cls, name, bases, attrs)

class Person(object):
    __metaclass__ = Hasher
    def __init__(self, fName, lName):
        self.fName=fName
        self.lName=lName

print Person.hash

# this is the last line of the file :)
