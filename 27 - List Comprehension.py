# List Comprehension:-
l = [100,200,300,400,500]
l2 = []
""" For getting square of every element in another List as we have studied by method - 1 """
for value in l:
    l2.append(value*value)
print(l2)#[10000, 40000, 90000, 160000, 250000]

"""in the terms of List Comprehension """
l = [100,200,300,400,500]
l2 = [value*value for value in l]
print(l2)# [10000, 40000, 90000, 160000, 250000]

l = [10,20,25,30,35,60,70,85]
l2 = [value for value in l if value%2 == 0]
print(l2)#[10, 20, 30, 60, 70]

l = ['abc','Shubh','bra','mitu','Bu']
l2 = [len(value) for value in l]
print(l2)#[3, 5, 3, 4, 2] So performance of List Comprehension is better than for loop

l2  = [(value1,value2) for value1 in range (1,5) for value2 in range (100,103)]
print(l2) # [(1, 100), (1, 101), (1, 102), (2, 100), (2, 101), (2, 102), (3, 100), (3, 101), (3, 102), (4, 100), (4, 101), (4, 102)]
""" So we can also apply concept of nested loop conditions in pyton programming language"""

l = [[1,2,3],[4,5,6],[7,8,9]] 
"""Convert it into l2 = [1,2,3,4,5,6,7,8,9] by using List Comprehension"""
l2 = []
for value in l:  #print(value) #[1, 2, 3] #[4, 5, 6] #[7, 8, 9]
     
   for val2 in value: #print(val2)
       l2.append(val2)
print(l2)# [1, 2, 3, 4, 5, 6, 7, 8, 9]
""" So finally..
l2 = [val2 for value in l for val2 in value]
print(l2)
"""

l = [100,105,110,115,120,125,130]
#Determine that which is even and which is odd by the help of list comprehension

l2 = ["Even" if value%2 == 0 else "odd" for value in l]
print(l2)# ['Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even']



""" About Dictionary Compehension also...."""


# Print a list as 1:1,2:4,3:9,4:16 by using list comprehension
d = {x:x**2 for x in range(1,11)}
print(d)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# print all characters with their ASCII values by using List Comprehension
# 'a':97,'b':98,'c':99......'z':122
d = {chr(x) : x for x in range(97,123)}
print(d)# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

# it will swap into a dictionary and mentiones as key & Valuepairs
d2 = {value:key for key,value in d.items()}
print(d2)# {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}

















































   
















































        








      
     

