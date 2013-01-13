#!/usr/bin/env python
import sys

if len(sys.argv) > 1 and sys.argv[1] == '-v':
  with open(sys.argv[0]) as me:
    print me.read()

n=6

def fib():
  a=0
  b=1
  while True:
    yield b
    c=b
    b+=a
    a=c

cnt=1
for i in fib():
  print i
  cnt+=1
  if cnt > n:
    break

#this is the last line of the file :)
