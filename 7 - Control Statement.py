#Looping in Python:-
"""Iterable Elements:- (str,list,tuple,dict,range,set)
Syntax Format:-
for [variable_name] in [iterable Datatype]:
statements
"""
l = [10,20,30,40,50]
"""print(l)"""
for value in l:
    print(value)

"""sum = 0+10 = 10
      10+20 = 30
      30+30 = 60
      60+40 = 100
      100+50 = 150
"""
sum = 0
for value in l:
    sum = sum+value
    print(sum)

"""In python:- there is a function called Range
range(5) = 0 1 2 3 4
range(10,100) = 10 11 12 13 14 15 ......99
range(10,100,5) = 10 15 20 25 30 35 ....90 95 100
"""

for value in range(5):
    print(value)
 # Here if we want to print 0 to 4 then write 5 in range because it prints from 0 to n-1 (where n= entered range)   
for shubham in range(20,100):
    print(shubham)
for value in range(10,100,5):
    print(value)
 # Here i wan tot start from 10 and print till 100 but i want difference of 5

sum = 0
for value in range(1,21):
    sum = sum+value
    print(sum)
    
    
    

