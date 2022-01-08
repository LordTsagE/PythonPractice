# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = input("a: ")
b = input("b: ")
# the new variable should be equal to the given one
c=(a)
#same here
d=(b)
#So when you switch them around, you don't affect the given one 
#in a way that fixes the second one you are 
#about to change as the first one
a=(d)
b=(c)
print("a: " + a)
print("b: " + b)