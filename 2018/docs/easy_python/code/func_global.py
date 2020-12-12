#!/usr/bin/env python
# Filename: func_global.py

def func():
	global x

	print 'x is',x
	x=2
	print 'Changed local x to',x

x=50
func()
print 'Value of x is',x

