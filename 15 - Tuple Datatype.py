#About Tuple Data Type:-
"""
# Tuple is also uses for stored different type of datatypes inside small brackets()
#but, the only difference between listand tuple is that , tuple is "IMMUTABLE" datatype which means i cannot add,update and delete the stored data
1) If we have parenthesis then it's tuple
2) Tuple is different from list because tuple is "IMMUTABLE" Datatype, So we can't Add,update and Delete for elements in tuple
3) It's also a Orderd DataType, So it's suppose to Indexing & Slicing:-
"""
t = (10,20,30,40,50)
print(t,type(t))#(10, 20, 30, 40, 50) <class 'tuple'>
help(tuple)
"""Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  #count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  #index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

[Finished in 177ms]
"""
#It shows that there are only two operations in tuplle that is :- Count & Index. No Addtion,updation & Deletion possible
t = (10,20,30,40,50)
#print(t[10])#IndexError: tuple index out of range
print(t[ :3])#(10, 20, 30)
t = (10,20,20,20,30,30,40,50)
print(t.index(20))#1 ( It gives priority to first occurance )
print(t.count(20))#3


l = [10,20,30,40,50]
for value in l:
    print(value)"""
10
20
30
40
50 """


