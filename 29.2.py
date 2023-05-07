def printVal(l):
    for value in l:
        yield value

l = [10,20,30,40,50,60]
g = printVal(l)
print(next(g))# 10
print(next(g))# 20
print(next(g))# 30
print(next(g))# 40
print(next(g))# 50
print(next(g))# 60 untill here it was present in list, what happend now, if i print again the same command
#print(next(g))# StopIteration ( So it's showing that StopIteration ) So, inn case of generator we have to handle it by try and except block, ( while ) in case of normal for loop it indicates atomatically

l = [10,20,30,40,50,60]
l2 = [value * value for value in l]
print(l2)# [100, 400, 900, 1600, 2500, 3600] as we have disccused in list but when this big bracket is converted into parenthesis

l2 = (value * value for value in l)
print(l2)# <generator object <genexpr> at 0x00000000030780C8> now we can get next output one by one by using simple repeating command
print(next(l2))# 100
print(next(l2))# 400
print(next(l2))# 900
print(next(l2))# 1600
print(next(l2))# 2500
print(next(l2))# 3600
# So by the generator we can create a output t a time that's it's a best way to save our meory in python programming language
















