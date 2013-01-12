#!/usr/bin/env python
import sys

print open(sys.argv[0]).read()

class animal:
    def __init__(self):
        print 'animal.__init__ called'
    def index(func):
        print 'animal.index called on function "' + str(func.__name__) + '"'
        zoo=[]
        func.index=True
        if func not in zoo:
            zoo.append(func)
        print 'zoo', zoo
        return func
    @index
    def cat():
        print 'animal.cat called'
        return 'cat'
    @index #won't work
    def dog(self):
        print 'animal.dog called'
        return 'dog'

print '\nfred=animal()'
fred=animal()
print '\nprint animal.cat.index'
print animal.cat.index
print '\nprint fred.dog()'
print fred.dog()
print '\nfred.dog.index'
print fred.dog.index

print '\ntrying animal.cat()'
try:
    animal.cat()
except TypeError as e:
    print 'fail:', e

#this is the last line of the file :)
