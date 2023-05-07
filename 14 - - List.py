#Update & Delete operation in list:-
#Update:-
l = [10,20,30,40,50]
l[2] = 420
print(l)#[10, 20, 420, 40, 50]

#PoP:-
l = [10,20,30,40,50]
r = l.pop()
print(l,r)#[10, 20, 30, 40] 50
#For pop out any perticular elemnt sinmply mention its index
l = [10,20,30,40,50]
r = l.pop(2)
print(l,r)#[10, 20, 40, 50] 30


#Remove:-
l = [10,20,30,40,50]
l.remove(20)
print(l)#[10, 30, 40, 50]
#If there is more than one 20 in give list
l = [10,20,20,30,30,20,40,50]
l.remove(20)
print(l)#[10, 20, 30, 30, 20, 40, 50]# It will remove only one occurance at a time for remove n 20's call n time command l.remove(20)
l.remove(20)
print(l)#[10, 30, 30, 20, 40, 50]


#clear:-
l = [10,20,30,40,50]
l.clear()
print(l)#[]
"""del l
print(l)#NameError: name 'l' is not defined"""


#Built In Functions For List:-
l = [50,40,30,20,10]
print(l.sort())#None ( if i run the code after this line it wil give me output none becase on writting sort it will execute defaulty and print(l.sort) so no sorted list untill now so can't print that's why shows none
print(l)#[10, 20, 30, 40, 50]
#2)
l3 = sorted(l)
print(l3)#[10, 20, 30, 40, 50]
"""For Reverse:-"""
#1)
print(l[ : :-1])#[50, 40, 30, 20, 10]
#2)
l.reverse()
print(l)#[50, 40, 30, 20, 10]


#index:-
l = [50,40,30,20,10]
print(l.index(30))#2
# in case there is multiple 30's in the list so it will give prreference to first occurance
l = [50,40,30,30,20,30,10]
print(l.index(30))#2
print(l.count(30))#3 ( It count the total number of occurance

l = [10,20,30,40,50,60]
l2 = [100,200,300,400,500]
print(l+l2)#[10, 20, 30, 40, 50, 60, 100, 200, 300, 400, 500]
# On adding two lists it will concatenates
#Here  1 and l2 are not modifying like EXTEND
l = 5
print(l * 10)#50
#but in list fornmat we can print till n times by multiplying n
l = [5]
print(l * 10)#[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


      
























