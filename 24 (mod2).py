import mod1
""" 120
True
True
True
"""
#_Pycache_
l = [100,200,300,400,500]
key = 500
print(mod1.binary_search(l,key))#True

l = [100,200,300,400,500]
key = 5000
print(mod1.binary_search(l,key)) #False



import math
help(math) # It will give a proper documentation of math command

import mod1
help(mod1)
""" Description :-
Help on module mod1:

NAME
    mod1 - If a function call it self again and again is known as recursive function

DESCRIPTION
    factorial(5) = 5 * fact(4)
                           4 * fact(3)
                               3 * fact(2)
                                       2 * fact(1)
                                               1

FUNCTIONS
    binary_search(l, key)
    
    factorial(num)

DATA
    key = 100
    l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    num1 = 5
    result = True

FILE
    
"""
# For adding the more details(description) in this help command of mod1 go to the actual mod1 file and add some docstrings. By the use of Docstring we can add any information by initialize it on starting. And by use Strings """.....""" any infor of any place inside function can be stored 
"""
Help on module mod1:

NAME
    mod1

DESCRIPTION
#    Docstring:- This Module Contains Binarty Search Implementation
#    Docstring command is description of that particular module

FUNCTIONS
    binary_search(l, key)
    
    factorial(num)

DATA
    key = 100
    l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    num1 = 5
    result = True

FILE

"""
help(mod1)


#package:- Packages is nothing but python directory
__init__.py
# So now this folder is bocome responsible for python directory




