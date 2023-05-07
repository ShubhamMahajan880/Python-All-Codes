# 4)Variable Length possoitional Arguements:-
l = [100,200,300,400]
l.append(500) 
print(l) # [100, 200, 300, 400, 500]
#l.append(500,250)
#print(l) #TypeError: append() takes exactly one argument (2 given)
""" So by append command we can add only one value in list """
""" By a single function  we can add more than a lots value"""
def add_value(*args):# here * is necessary to add the values at a time otherwise it will not works
    print(args)
  
add_value(100,200,300,400,500) # (100, 200, 300, 400, 500)

add_value(100,200) # (100, 200)

add_value(100,200,300,400,500,600,700,800) # (100, 200, 300, 400, 500, 600, 700, 800)

def add_value(*args):
    l = []
    for value in args:
        l.append(value)

    return l

result = add_value(100,200,300,400,500) #[100, 200, 300, 400, 500]
print(result)
result = add_value(100,200)# [100, 200]
print(result)
result = add_value(100,200,300,400,500,600,700,800) #[100, 200, 300, 400, 500, 600, 700, 800]
print(result)


# 2) variable Length keyword Arguement:-

def get_details(**kwargs): #Key Word Arguments ( here double star (**) is necessary to get all the keys and value pairs
    print(kwargs)

get_details(name="ABC",email="abc@gmail.com",Contact="9669999880",dob="26-06-2002")# by uisng it we can print every key word 
#{'name': 'ABC', 'email': 'abc@gmail.com', 'Contact': '9669999880', 'dob': '26-06-2002'}
 


 





