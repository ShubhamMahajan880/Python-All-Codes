# Intertools and Iterators in Python Programming Language :-
l = [100,200,300,400,500]
i = iter(l) # iter method is used to creating a iterator over this
print(l)# [100, 200, 300, 400, 500]
print(next(i))#100
print(next(i))#200

for value in i:
    print(value)
"""
100
200
300
400
500
"""
import itertools

l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000] # if i want to iterating over list l1 l2 and l3 at atime then we can use here chain method which is inside itertools command or library

i = itertools.chain(l1,l2,l3)
print(i)# <itertools.chain object at 0x000000000305FCC8>
print(next(i))# 10 so by this command we have to type and run it agian and again
for value in i:
    print(value)
"""
10
20
30
40
50
100
200
300
400
500
1000
2000
3000
4000
5000
So by this itertool and chain method after using for loop we can easily print more than 1 list at a time
"""
# if i want that a list iterated continuosly more time agian and agian then i have to needd to create a "ITERATOR"
# for performing this task we use a method called as "CYCLE METHOD"  By applyting only cycle command it will iterating infinite time so for soppinf this we have to use any condition
l = [10,20,30,40,50]
count = 0
for value in itertools.cycle(l):
    if count < 20:
        print(value)

    else:
        break
    count+=1
"""
10
20
30
40
50
10
20
30
40
50
10
20
30
40
50
10
20
30
40
50
>>>
So this has count till 20(elements appear after executing again and again )
"""
# If you want same list multiple times in every iteration then instead of "cycle" I can use "REAPEAT"
l = [10,20,30,40,50]
count = 0
for value in itertools.repeat(l):
    if count<20:
        print(value)
    else:

        break
    count+=1
"""
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
So by this command we obtained same list agian and again till gieven condition here is 20
"""

l = [10,20,30,40]
i = iter(l)

for value in i:
    print(value)

#print(next(i))# StopIteration ( So, on using this command this time it's showing th eroor that stop iteration because all the elements are already be appeared in same order )
# So for execute the same list agaain after running one time we can use here "tee" method

l = [10,20,30,40,50]
i = iter(l)
t  = itertools.tee(i)
print(t)# (<itertools._tee object at 0x00000000030263C8>, <itertools._tee object at 0x000000000305FE08>)
for value in t[0]:
    print(value)
"""
10
20
30
40
50
"""
for value in t[1]:
    print(value)
"""
10
20
30
40
50
""" # So this method of "tee" helpus to iterate over the same list again
# if i want to create multple objects then it wll iterate that objects:-
l = [10,20,30,40]
i = iter(l)
t = itertools.tee(i,5)
print(t)
"""
(<itertools._tee object at 0x000000000305FC08>, <itertools._tee object at 0x0000000003074D08>, <itertools._tee object at 0x0000000003074C48>, <itertools._tee object at 0x0000000003074D88>, <itertools._tee object at 0x0000000003074C88>)
So it's ietrating for 5 objects """

# if in list or more than one list i want to iterate over fix no of elements then it can be done by method "ISLICE"
l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]

i = itertools.chain(l1,l2,l3)
for value in itertools.islice(i,0,8): # mention the initializing element no. and finalizing element number )
    print(value)
"""
10
20
30
40
50
100
200
300
 So by isclice we can print selected elements from initial number to the final number"""

#range(10,50) by this range mthod i can print from a specific poit to a specific point but can't ptint till infinity
# That's why in itertools metho we have a command names as "COUNT" by which we can print till infinite numbers easily
count = 0
for value in itertools.count(10,5):
    if count > 20:
        break
    else:
        print(value)
    count+=1
""" for value in itertools.count():
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20 ( when no any value in parenthesis it will print till the condition and if the condition is not here then can be print till infinity
"""
""" for value in itertools.count(5):
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
>>
"""
""" for value in itertools.count(10,5): ( means it will start the counting from 10 and print till 20 terms by the difference of 5 )
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
105
110
>>>
"""
# Next method in itertools technique is "P & C" :-
l = [1,2,3,4,5,6]
print(itertools.permutations(l,2))# <itertools.permutations object at 0x000000000304E6A8>
print(list(itertools.permutations(l,2))) # For getting that permutation pairs
"""
[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)]
"""
print(list(itertools.combinations(l,2)))
"""
[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]
"""














































