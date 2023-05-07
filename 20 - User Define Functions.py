#User Defined Funtions in Python Programming Language
""" Why needed:-
1) Code Reuse
2) Modularity
"""

s = "pyhton"
print(s[ : :-1])#nothyp

""" Same concept  by using function definition and function call"""
def value_reverse(value): #Value_reverse is name of function we have to use.after def write name of the function and in paranthesis write result which is to be find
    reverse = value[ : :-1]
    print(reverse)
# This was about function defination(def)
s = "python"
result = value_reverse(s) #nothyp 
#And ths was about function calling
#Python can't execute the function without calling it,so if we remove function calling then it will not executed

def value_reverse(value): #Value_reverse is name of function we have to use
    reverse = value[ : :-1]
    return reverse
s = "python"
result = value_reverse(s)
print(result) #nothyp
 
l = [100,200,300,400]
result = value_reverse(l)
print(result)#[400, 300, 200, 100]

"""num = 100
result = value_reverse(num) # our striding operation  is not work for integer
print(result) #TypeError: 'int' object is not subscriptable """
# So for these there is some modifications in pythoncalling:-                                               
def value_reverse(value):
    if type(value)==list or type(value)==str:
        reverse = value[ : :-1]
    else:
        temp = str(value)
        reverse = temp[ : :-1]
    return reverse

num = 100
result = value_reverse(num)
print(result) #001





