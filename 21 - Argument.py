# 1) Positional Arguments:-
def linear_search(l,key): # and, in function definition also have two values
    for value in l:
        if key==value:
            return True
    else:
        return False
l = [100,200,300,400,500]
#key = 400     True
key = 4000
result = linear_search(l,key) # So, in a function we are passing two values
print(result) #False
"""#if we pass one value then it throws the error
result = linear_search(l)
print(result)  # linear_search() missing 1 required positional argument: 'key'
"""

 # If the total number of arguements in functiona callling and function definition are same then that arguement system is calles as "Possitional Argument" system
 # In this it is mandatory that no of values of fucntion calling shoulb be equal to no of values in function definition

# 2) Default Arguements:-
""" i want to generate a password containing:-
8 char
1 upper
1 lower
1 special char
5 digits 
"""
# for this we use two functions "ord" & "chr"
print(ord('a'),ord('z')) #97 122 ( ord is uses for converting in ASCII Values )
print(ord('A'),ord('Z')) #65 90 
print(chr(97)) #a ( chr is uses for getting character from entered ASCII Value )



 


import random
def gen_password():
    l = ['@','#','$','&']

    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit)
    return password

result = gen_password()
print(result) #Al#73941
#Bg@70417
#Ze@91066 
#Lt$44653 bu default generated password have length of 8



def gen_password():
    l = ['@','#','$','&']

    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit)
    l = random.sample(password,length)
    #password = ("").join(l)
    print(l)
    return password
    result = gen_password(5)
    print(result) 
 
# 3) Keyword Argument:-
""" i wan tto check that entered password is a valid password or not:-"""

def validate(username,password):
    if username =="ABC" and password =="Abc@123":
        print("Valid Password")
    else:
        print("Invalid Password")

validate("ABC","Abc@123") #Valid Password
validate("Abc@123","ABC") #Invalid Password ( in this case it is showing Invalid password because here order is matter )
validate(password="Abc@123",username="ABC") #Valid Password  ( when we define parameters then order dosn't matter )

help(print)
"""
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

"""

print(100,200) #100 200
print("Hi") #Hi

print(100,200,sep=",",end=" ")
print("Hi") #100,200 Hi












































\





