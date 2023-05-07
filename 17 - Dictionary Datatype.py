#Dictionary Datatype Update & Delete Operation:-
l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]
d = dict(zip(l1,l2))
print(d)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25} [ By using these command we can convert two lists into dictionary, one(first) list behave as keys and another(second) list behave as Value-Pairs. so conversion of a single list into dictionary is not possible


#Conversion of a single list into dict
l = [1,2,3,4,5]
d = dict.fromkeys(l)
print(d)#{1: None, 2: None, 3: None, 4: None, 5: None} [ by default valuepair is none ]
d = dict.fromkeys(l,1)
print(d)#{1: 1, 2: 1, 3: 1, 4: 1, 5: 1} [ by assigning a single value pair it will a lot to all keys that value ]


#For Merge Two Dictionaries:- ( we use UPDATE command )
d1 = {1:1,2:4,3:9,4:16}
d2 = {5:25,6:36}
d1.update(d2)
print(d1)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}


#For Deletion of dictionaries:- ( we use POP,POPITEM,CLEAR commands )

#for delete any particular key & Valur Pair
r = d1.pop(2)
print(d1)#{1: 1, 3: 9, 4: 16, 5: 25, 6: 36}
print(d1,r)#4 [ shows the value removed from dict ]
r = d1.popitem()
print(d1,r)#{1: 1, 3: 9, 4: 16, 5: 25} (6, 36) [ popitem remove last key&valuepair  defaultly ]

#For delete entire the dictionary:-
d1.clear()
print(d1)#{}




















