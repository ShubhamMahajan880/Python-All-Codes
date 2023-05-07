#Recursuve Function in python:-
""" If a function call it self again and again is known as recursive function

factorial(5) = 5 * fact(4)
                       4 * fact(3)
                           3 * fact(2)
                                   2 * fact(1)
                                           1   """ # Such a problems can be easily solve by recursion
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

num1 = 5
result = factorial(num1)
print(result) # 120

""" About Binary search:-
l = [100,200,300,400,500,600,700,800,900]
key = 700

mid  = 9/2 = 4 = 500 == 700 True ( Here in division ignore the decimal part )

( Since it's an sorted array that's why we can say that if element is Greater than mid then it will be present at Right Hand Side of mid similarly if the element is lesser than mid then it will be present at Left Hand Sidde of mid

[600,700,800,900] 

mid = 4/2 = 2
800 == 700

[600,700]
mid = 2/2 = 1

700 == 700 return True
"""

def binary_search(l,key):
    mid = len(l)//2 # Here we want mid as integer format only that's why we used Floor division operator here

    if l[mid] == key:
        return True

    elif key < l[mid]:
        return binary_search(l[:mid],key)#Since key element is less than mid tha's why it will be present at L.H.S. of mid So use slicing anf initialize from zero to  mid 
    else:
        return binary_search(l[mid+1:],key)# initialize from mid+1 to end of the list

l = [100,200,300,400,500,600,700,800,900]
key = 700

result = binary_search(l,key)
print(result)#True ( So it's working )

l = [100,200,300,400,500,600,700,800,900]
key = 100

result = binary_search(l,key)
print(result)#True ( So it's working )

"""
l = [100,200,300,400,500,600,700,800,900]
key = 1000 

result = binary_search(l,key)
print(result) #IndexError: list index out of range
"""




                                           


def binary_search(l,key):

    if len(l) == 0:
        return False
    else:
        
        mid = len(l)//2 # Here we want mid as integer format only that's why we used Floor division operator here   
        if l[mid] == key:
            return True

        elif key < l[mid]:
            return binary_search(l[:mid],key)#Since key element is less than mid tha's why it will be present at L.H.S. of mid So use slicing anf initialize from zero to  mid 
        else:
            return binary_search(l[mid+1:],key)# initialize from mid+1 to end of the list

l = [100,200,300,400,500,600,700,800,900]
key = 100
result  = binary_search(l,key)
print(result) # True














