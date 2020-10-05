# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:24:36 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function： Lambda Expressions

"""
def make_incrementor(n):
         return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

#%% Documentation Strings
def my_function():
   """Do nothing, but document it.

     No, really, it doesn't do anything.
   """
   pass
print(my_function.__doc__)