# Datatypes Understanding:-

#1) int:-
num1 = 100
print(type(num1))
#2) Float:-
num2 = 15.25
print(type(num2))

# Int and Float both are IMMUTABLE datatypes
#Inpython each value is stored at different memory allocation that's why each have different id's so int & float are IMMUTABLES
num1 = 125
print(id(num1))
num2 = 105
print(id(num2))

#3) String:- ' ', "  ", " " "
""" 1) Strings are Immutable
 2) String is ordered data structure and supports to indexing & Slicing """
s = "Iam Learning Python"
print(id(s))
print(s,type(s))

#4) List:- []
# List is a datatype in which we can sotre the data,everything which is inside square brackets[] is list
# Python list is HETROGENEOUS in which i can store different type of data it may be int,float as well as string
#Python list is a "MUTTABLE" datatype in which i can add,update and delete the stored data at the same memory location means id dosnt't change while remaining same
""" 1) List are Muttable we can add,Update,Delete
2) Ordered Datatype means includes Indexing & Slicing
3) It is a Hetrogeneous Datatype, I can store any time of Data inside it
"""
l = [10,20,30,40,50,60,"Artificial Intellegence","Machine Learning"]
print(l)
print(id(l))
l.append(70)
print(id(l))

#5) tuple:- ()
""" 1) If we have parenthesis then it's tuple
2) Tuple is different from list because tuple is "IMMUTABLE" Datatype, So we can't Add,update and Delete for elements in tuple
3) It's also a Orderd DataType, So it's suppose to Indexing & Slicing:-
"""
# Tuple is also uses for stored different type of datatypes inside small brackets()
#but, the only difference between listand tuple is that , tuple is "IMMUTABLE" datatype which means i cannot add,update and delete the stored data
t = (10,20,30,40)
print(t)

#6) Dict:-
""" 1) Dictionary is  "MUTTABLE"
2) Dict is Unordered, so indexing & Slicing are not possible
3) Key should be unique we can't make a duplicate key
4) Key should be Immutable datatypes like (int,float,str,tuple)
5) It have Average Time complexity is O(1) that's why it's fater in fatching the values
"""
# Dict is also uses for stored different type of datatypes inside middle brackets{}
#python stores the value in "key" and "valuepairs" it's also called as "HASHMAPS"
#In this key and valupairs are seperated by comma, wheres key and valupairs are written in string using column:
d = {"Scientist":"ShubhamMahajan","ArtificialIntellegencyScholar":"ShubhamMahajan"}
print(d)
print(d["Scientist"])

#7) Set:- {}
""" 1) A python set is a unordered collection of elements and using which we can perform various set operations like:- Union,Intersection,Difference on the elements
2) Sets are MUTTABLE
3) All the elemts should be unique and duplicates elemens not exist
4) Only IMMUTABLE elements can be added like int,float,tuple,str
5) It's an unorderdd datatype so Indexing & Slicing cannot be performed
"""
# Set is also uses for storing data in various datatypes inside the curely brackets {}
# Set is also a "MUTTABLE" Datatypes which means we can Add, Update and Delete the elemets
# By using set i can perform all the set operations like Union,Intersection,Symmetric Difference
s = {10,20,30,40,50}

#8) bool:-
# Specified as TRUE & FALSE which are result not mentioned in strings

#9) Complex Datatypes:-
#Uses for representing the real and imaginary paths
u = 4+3j
print(u)
print(type(u))

help(str)














