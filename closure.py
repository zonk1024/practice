#!/usr/bin/env python
print 'def shifter(a):'
print '  assert type(a) == int'
print '  def times(b):'
print '    assert type(b) == int'
print '    return a<<b'
print '  return times'

def shifter(a):
  assert type(a) == int
  def times(b):
    assert type(b) == int
    return a<<b
  return times

print 'z=shifter(2)'
z=shifter(2)
print 'z(10-1)'
print z(10-1)
