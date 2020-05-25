#!/usr/bin/env python
# Filename: reference.py

print 'Simple Assignment'
shoplist=['apple','mango','carrot','banana']
mylist=shoplist # mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print 'Copy by making a full slice'
mylist=shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that now the two lists are different

