#About MAP,FILTER & LAMBDA functions in Python Programming Language :-

l = [10,20,30,40,50,60]
# Want square of every element as list by using map
# Map :- Map is a function which takes another functtion as argument and takes iterable as second argument
def sqr(num1):
    return num1**2

l = [10,20,30,40,50,60]
result = map(sqr,l)
print(result)# <map object at 0x000000000305FDC8>
result = list(map(sqr,l))#typecasting using list 
print(result)# [100, 400, 900, 1600, 2500, 3600]
"""for value in result:
    print(value) 
100
400
900
1600
2500
3600
"""

# Addition of elements of two lists using map function
def add(num1,num2):
    return num1+num2

l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]
result  =list(map(add,l1,l2))
print(result)# [110, 220, 330, 440, 550]

#Identify the even numbers by using FILTER functions :-
def check_num(num1):
    if num1%2 == 0:
        return True
    else:
        return False # at place of return False if i write return 1 then it uses for true, so here it will print all the numbers even as well as odd
l = [100,115,120,125,130,135,140]
result = list(filter(check_num,l))
print(result)# [100, 120, 130, 140] It will only filtr the result for which answer is true if the answer is false it will not return it

 # Same opration by map function:-
result = list(map(check_num,l))
print(result)# [True, False, True, False, True, False, True]

#lambda Function:- lambda functin is also called as "Anonymous Function", whenever their is a feew lines of code then instead of map and filter we can seperatly define a different function csll by using lambda function

"""l = [10,20,30,40,50,60]
result = list(map(lambda num1:num1**2,1))
print(result) """

l = [100,115,120,125,130,140]
result = list(filter(lambda num:num%2 == 0,l))
print(result) # [100, 120, 130, 140]

d = {1:50,2:40,3:30,4:20,5:10}
l = sorted(d)
print(l)# [1, 2, 3, 4, 5] it is only giving us keys and we want to take key as well as value pair also
l = sorted(d.items())
print(l)# [(1, 50), (2, 40), (3, 30), (4, 20), (5, 10)]

d  = {8:50,3:40,2:30,1:20,5:10}
l = sorted(d.items())
print(l)# [(1, 20), (2, 30), (3, 40), (5, 10), (8, 50)] It is sorted on the basis of key not on the basis of valuepairs, so there is need of one more argument to sort exactly

d  ={8:50,3:40,2:30,1:20,5:10}
l = sorted(d.items(),key=lambda x:x[1])
print(l)# [(5, 10), (1, 20), (2, 30), (3, 40), (8, 50)] If a i want to in terms of dictinary then agian use typecasting
l = dict(sorted(d.items(),key=lambda x:x[1]))
print(l)# {5: 10, 1: 20, 2: 30, 3: 40, 8: 50}




















































    
