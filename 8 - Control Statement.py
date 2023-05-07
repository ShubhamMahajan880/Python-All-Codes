#Iterating Using For Loop :- Break,Continue,Enumerate
l = [10,20,30,40,50,60]
key = 400
for value in l:
    if value == key:
        print("Element Found")
        break
    else:
        continue
else:
    print("Element not found")
#The above else represents that how this additional else works
print("Sattement after the for loop")

l = [10,20,30,40,50,60]
key = 50
for index,value in enumerate(l):
    print(index,value)
# Enumerate is uses for printing two values one is order and another is value at that order
    if value == key:
        print("Elemet found at index",index)
        break
    else:
        pass
    #print("Statement after continue statement")
else:
    print("Element not found")

for i in range(10):
    print(i)
for j in range(10,50):
    print(j)

for k in range(10,50,2):
    print(k)

for m in range(50, 10,-2):
    print(m)
    

    

    


    
    


    
    

