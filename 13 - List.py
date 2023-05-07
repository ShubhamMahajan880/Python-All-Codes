#List Datatype, Indexing, Slicing,Append-Insert-Extend:-
"""
List is a datatype in which we can sotre the data,everything which is inside square brackets[] is list
# Python list is HETROGENEOUS in which i can store different type of data it may be int,float as well as string
#Python list is a "MUTTABLE" datatype in which i can add,update and delete the stored data at the same memory location means id dosnt't change while remaining same
1) List are Muttable we can add,Update,Delete
2) Ordered Datatype means includes Indexing & Slicing
3) It is a Hetrogeneous Datatype, I can store any time of Data inside it

"""
l = [10,20,30,40,"Python","Java",[100,200,300]]
print(l,type(l))


#Indexing:-
print(l[0])#10
print(l[5])#Java
print(l[-1])#[100, 200, 300]
print(l[-1][0])#100
"""print(l[20])"""#list index out of range


#slicing:-
print(l[1:3])#[20, 30]
#at place of 3 here is 40 which si not inclusive
print(l[ : : -1])#[[100, 200, 300], 'Java', 'Python', 40, 30, 20, 10] ( IT reveerse the list )


l = [100,200,300,400,500]
for value in l:
    print(value)
"""
100
200
300
400
500"""
# On each iteration we get on element from this list, whenever we iterating over list we iterarating over elements while in terms of string we iterating over characters
for value in l[ : :2]:
    print(value)
"""
100
300
500 """

#Methods for inserting a new element in list:-
l = [100,200,300,400,500]
print(id(l))#44193928
l.append(600)
print(l)#l = [100,200,300,400,500,600]
print(id(l))#44193928
#Since id of list after adding an element is also remaining same bacause List are MUTTABLE at same memory location we are modifying the values
num1 = 100
print(id(num1))#8791238282608
print(id(l[0]))#8791238282608( So both the id's( Memory Locations ) are exact similar bacause list stores the refenrence of values


#Methods for adding multiple elements in list:- 1) Extend & Append Method:-
l = [100,200,300,400,500]
l.extend([500,600,700,800])
print(l)#[100, 200, 300, 400, 500, 500, 600, 700, 800]
l.append([500,600,700,800])
print(l)#[100, 200, 300, 400, 500, 500, 600, 700, 800, [500, 600, 700, 800]]
#So this is the deifference between extend and append that in case of APPEND it add as "[ONE ELEMENT]" in list while in case of EXTEND it adds all as "[INDIVIDuAL]"[ELEMENTS]"
#l.extend([500,600,700,800],100,200)#extend() takes exactly one argument (3 given)
#l.append([500,600,700,800],100,200)#append() takes exactly one argument (3 given)
#So in both we can add only one arguement
l.extend("Python")
print(l)#[100, 200, 300, 400, 500, 500, 600, 700, 800, [500, 600, 700, 800], 'P', 'y', 't', 'h', 'o', 'n']
#it will iterating over character by character over the string

""" 2) By Insert Method:-"""
l = [100,200,300,400,500]                                                        
l.insert(1,1000)
print(l)#[100, 1000, 200, 300, 400, 500]
#by insert method it add element on index plce
#by insert method we can add ONLY ONE element not more than one
l = [10,20,30]
l2 = l
print(id(l),id(l2))#50708616 50708616
print(l,l2)#[10, 20, 30] [10, 20, 30]
#Many time there is a need for copy content from one list to another list, there is no change in Memory Allocation
l.append(40)
print(l,l2)#[10, 20, 30, 40] [10, 20, 30, 40]
print(id(l),id(l2))#51408456 51408456



















  
    
    
    








