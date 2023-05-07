#Set Datatype in Python:-
"""
# Set is also uses for storing data in various datatypes inside the curely brackets {}
# Set is also a "MUTTABLE" Datatypes which means we can Add, Update and Delete the elemets
# By using set i can perform all the set operations like Union,Intersection,Symmetric Difference
1) A python set is a unordered collection of elements and using which we can perform various set operations like:- Union,Intersection,Difference on the elements
2) Sets are MUTTABLE
3) All the elemts should be unique and duplicates elemens not exist
4) Only IMMUTABLE elements can be added like int,float,tuple,str
5) It's an unorderdd datatype so Indexing & Slicing cannot be performed
"""
s = {10,20,30,40}
print(s,type(s))#{40, 10, 20, 30} <class 'set'>
#onadding duplicate values in set
s = {10,20,30,40,10,20,30,40}
print(s)#{40, 10, 20, 30} [ It's not printing in order shows that duplicate elements can't be added ]
#adding new element through command
s = {100,200,300,400}
s.add(500)
print(s)# {100, 200, 300, 400, 500}


#Operation on Sets:-
s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}
s3 = s1.union(s2)
print(s3)#{70, 40, 10, 80, 50, 20, 90, 60, 30}
s3 = s1.intersection(s2)
print(s3)#{40, 50, 60}
s3 = s1.difference(s2)#The only elements present in set s1 but not in set s2
print(s3)#{10, 20, 30}
s3 = s2.difference(s1)
print(s3)#{80, 90, 70}
s3 = s1.symmetric_difference(s2)#The unique elements which in set 1 and set 2 and not common in both
print(s3)#{70, 10, 80, 20, 90, 30}
print(s1)#{40, 10, 50, 20, 60, 30}
s1.update(s2)
print(s1)#{70, 40, 10, 80, 50, 20, 90, 60, 30} [ In case of union perform union operation and return the result which can assign in terms of any third variable , In case of "UPDATE" opertion it will perform the unioon but not return anything hat menas it modify the original set s1 ]
s1.intersection_update(s2)
print(s1)#{70, 40, 80, 50, 90, 60}

















