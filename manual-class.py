#!/usr/bin/env python

superclasses=(object,)

def init(self, fName, lName):
    self.fName=fName
    self.lName=lName
def fullName(self):
    return self.fName + ' ' + self.lName

attrs={
    '__init__': init,
    'fullName': fullName,
    'race'    : 'human',
}

Person=type('Person', superclasses, attrs)

#class Person(object):
#    race='human'
#    def __init__(self, fName, lName):
#        self.fName = fName
#        self.lName = lName
#    def fullName(self):
#        return self.fName + ' ' + self.lName

bob=Person('bob', 'bobbers')
print bob.fullName()
print bob.race
