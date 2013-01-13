#!/usr/bin/env python
#this is a silly caching example for decorators.
#the idea is that if you are calling monkey or
#lion it will sleep (as if processing), but if
#monkey (decorated with @zoo) has been called
#before than we know what the return value is
#already, and we can just return it because it
#is stored as a property now.
#update -- added cache ttl
#update -- gave ttl multiplier argument to zoo

import sys, time

slow=2
if len(sys.argv) != 1 and sys.argv[1] == '-v':
    with open(sys.argv[0]) as me:
         print me.read()

class animal:
    def __init__(self):
        print 'animal.__init__ called'
    def zoo(duration):
        print 'zoo called, with duration argument of', duration
        def cage(func):
            print 'cage called on function:',  func.__name__
            def checkZoo(self):
                print 'checkZoo called'
                if not hasattr(func, 'ret'):
                    func.ret=(func(self), time.time())
                elif time.time() - func.ret[1] < slow * duration:
                    print func.__name__, 'found in cache and fresh'
                else:
                    print func.__name__, 'found in cache, but expired'
                    func.ret=(func(self), time.time())
                return func.ret[0]
            return checkZoo
        return cage
    def lion(self):
        print 'lion called -- "processing"'
        time.sleep(slow)
        print 'lion done "processing"'
        return 'lion return'
    @zoo(1)
    def monkey(self):
        print 'monkey called -- "processing"'
        time.sleep(slow)
        print 'monkey done "processing"'
        return 'monkey return'


print '\nfred=animal()'
fred=animal()

print '\ntrying: print fred.lion()'
print fred.lion()

print '\ntrying again: print fred.lion()'
print fred.lion()

print '\ntrying again: print fred.lion()'
print fred.lion()

print '\ntrying: print fred.monkey()'
print fred.monkey()

print '\ntrying again: print fred.monkey()'
print fred.monkey()

print '\nsleeping, then trying again: print fred.monkey()'
time.sleep(slow*2)
print 'now trying: print fred.monkey()'
print fred.monkey()

#this is the last line of the file :)
