#Genrator Functions in Python Programming:-
def printVal(l):
    for value in l:
        print(value)
        
l = [10,20,30,40,50,60]
printVal(l) 

def fibo():
    first_num = 0
    second_num = 1
    yield second_num # 1 1 2 3 5 8
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num,next_val

g = fibo() # this commandis generating the fibonacci sequence for futrther series 
print(g)# <generator object fibo at 0x0000000003016348>

print(next(g))# 1
print(next(g))# 2
print(next(g))# 3
print(next(g))# 5
print(next(g))# 8
print(next(g))# 13

""" For getting Febonicci series till any n number"""
for value in range(10):
    print(next(g))
"""
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
""""
