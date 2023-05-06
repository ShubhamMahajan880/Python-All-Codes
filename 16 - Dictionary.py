#Conversion of "LIST" To "TUPLE" & "TUPLE" To "LIST"
l = [10,20,30,40,50]
t = tuple(l)
print(t,type(t))#(10, 20, 30, 40, 50) <class 'tuple'> This command is uses for conversion of list to tuple

t = ("a","b","c",100)
l = list(t)
print(l,type(l))#['a', 'b', 'c', 100] <class 'list'>



# Lecture 16:- Dictionary:-
"""
# Dict is also uses for stored different type of datatypes inside middle brackets{}
#python stores the value in "key" and "valuepairs" it's also called as "HASHMAPS"
#In this key and valupairs are seperated by comma, wheres key and valupairs are written in string using column:
1) Dictionary is  "MUTTABLE"
2) Dict is Unordered Datatype, so indexing & Slicing are not possible
3) Key should be unique we can't make a duplicate key
4) Key should be Immutable datatypes like (int,float,str,tuple)
5) It have Average Time complexity is O(1) that's why it's fater in fatching the values
"""

d = {"emp_id":101,"name":"shubham","Phone no.":"9669999880","GmailId":"shubhammahajan4@gmaicom"}
print(d)#{'emp_id': '101', 'name': 'shubham', 'Phone no.': '9669999880', 'GmailId': 'shubhammahajan4@gmaicom'}
#when in valuepair there is a int value it can be written without string format

#adding new key and value pair:-
d["Hobbe"] = "Learning Coding"
print(d)#{'emp_id': 101, 'name': 'shubham', 'Phone no.': '9669999880', 'GmailId': 'shubhammahajan4@gmaicom', 'Hobbe': 'Learning Coding'}

#geeting any value from dictionary's key
print(d.get("name"))#shubham
print(d.get("SEX"))#None (When something not exist and we want to get then it shoes "NONE")
print(d.get("SEX",-1))# -1 (when key is not defined and we want that key by providing some value through get function, it gives that value as result
print(d.setdefault("age"))
print(d)#{'emp_id': 101, 'name': 'shubham', 'Phone no.': '9669999880', 'GmailId': 'shubhammahajan4@gmaicom', 'Hobbe': 'Learning Coding', 'age': None}
# In get if the key exist then return the value otherwise none or -1 ,
# but in setdefault it check that key exist or not, if exist then return the value otherwise set that key in DICTIONATY and return with none or specified with default value
print(d.setdefault("age",50))


#How we can add values in an empty dictionary
d = {}
for value in range(1,11):
    d[value] = value*value

print(d)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

d = {"emp_id":101,"name":"shubham","Phone no.":"9669999880","GmailId":"shubhammahajan4@gmaicom"}
#For printing keys of dictionary:-
print(d.keys())#dict_keys(['emp_id', 'name', 'Phone no.', 'GmailId'])

#For printing all Value Pairs od Dictionary:-
print(d.values())#dict_values([101, 'shubham', '9669999880', 'shubhammahajan4@gmaicom'])

# & similarly for printing both the value pairs as well as key:-
print(d.items())#dict_items([('emp_id', 101), ('name', 'shubham'), ('Phone no.', '9669999880'), ('GmailId', 'shubhammahajan4@gmaicom')])

#For getting all items in seperated and tuple format:-
for t in d.items():
    print(t) 
    
    





