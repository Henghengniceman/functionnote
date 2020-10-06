# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:12:18 2020

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function： define function 

"""
from math import pi
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
def concat(*args, sep="/"):
         return sep.join(args)
"""
squares = list(map(lambda x: x**2, range(10)))
# equal 
squares = [x**2 for x in range(10)]
## 
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
## round can be used to show Decimal
[str(round(pi, i)) for i in range(1, 6)]
#%% zip list
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))





