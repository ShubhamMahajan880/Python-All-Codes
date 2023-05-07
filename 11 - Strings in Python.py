# Strings in Python Programming:-
"""
1) Strings are Immutable
2) String is ordered data structure and supports to indexing & Slicing
"""
s = "python"
print(type(s))
print(id(s))
print(s)

s = "java"
print(type(s))
print(id(s))
print(s)

d = "python"
print(type(d))
print(id(d))
print(d)

#indexing:- in this there are two categories:-1){Left Hand Side Indexing}:- In which indexing startted from left to right [ Where we start counting from indxing 0 ]
#                                             2){Right to Left Indexing} :- In which indexing started from right to left [ Where we count from -1 ]

s = "Python Sample String"
print(s[0])#p
print(s[-1])#g
print(s[1])#y
print(s[-2])#n

#Slicing:-
s = "Python Sample String"
print(s[0:5])#Pytho
print(s[0:6])#Python
print(s[7:])#Sample String (Started from 7 that is s of string and end is not mentioned so printed till last)
print(s[ :6])#Python (Since Start point is not mentioned so starting form zero by default)


#Stride:- is uses for printing of selected letters
# If the stride is possitive[+] it will give direction from left to right, negative[-] it will give direction from right to left
print(s[ : :2])#Pto apeSrn                (I do not want initialize:do not want to print end:but print every second letter)
print(s[ : :3])#Ph metn                   (after 1st lettere[P] every third letter will be print)

print(s[ : :-1])#gnirtS elpmaS nohtyP     ( negative indexing prints from right hand side, so in stride prints reversely )
print(s[ : :-2])#git lmSnhy ( after last first element it will print every second element from last )


# For printing ewvery letter of memtiones string
for value in s:
    print(value)
"""P
y
t
h
o
n
 
S
a
m
p
l
e
 
S
t
r
i
n
g """

# in such a way for iterating characters:-
for value in s[ : :2]:
    print(value)
"""P
t
o
 
a
p
e
S
r
n"""

help(str)








