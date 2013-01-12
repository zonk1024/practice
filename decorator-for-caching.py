#!/usr/bin/env python
#this is a silly caching example for decorators.
#the idea is that if you are calling monkey or
#lion it will sleep (as if processing), but if
#monkey (decorated with @zoo) has been called
#before than we know what the return value is
#already, and we can just return it because it
#is stored as a property now.

import sys, time

slow=2
if len(sys.argv) != 1 and sys.argv[1] == '-v':
    print open(sys.argv[0]).read()

class animal:
    def __init__(self):
        print 'animal.__init__ called'
    def zoo(func):
        print 'zoo called on function:',  func.__name__
        def checkZoo(self):
            print 'checkZoo called'
            if not hasattr(func, 'ret'):
                func.ret=func(self)
            else:
                print func.__name__, 'found in cache'
            return func.ret
        return checkZoo
    def lion(self):
        print 'lion called -- extra sleep'
        time.sleep(slow)
        print 'lion wake'
        return 'lion return'
    @zoo
    def monkey(self):
        print 'monkey called -- extra sleep'
        time.sleep(slow)
        print 'monkey wake'
        return 'monkey return'


time.sleep(slow)
print '\nfred=animal()'
fred=animal()

time.sleep(slow)
print '\ntrying: print fred.lion()'
print fred.lion()

time.sleep(slow)
print '\ntrying again: print fred.lion()'
print fred.lion()

time.sleep(slow)
print '\ntrying: print fred.monkey()'
print fred.monkey()

time.sleep(slow)
print '\ntrying again: print fred.monkey()'
print fred.monkey()

#this is the last line of the file :)
