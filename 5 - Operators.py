# Python Operators

#1)Arithmatic operators:-(+,-,*,/,//,**)
num1 = 10
num2 = 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(10/3)
# For getting only the "integer" part use " FLOUR DIVISION OPERATOR "
print(10//3)
# For getting reminder use modulus operator (%)
print(10%3)
# For power use " POWER OPERATOR " (**)
print(10**2)

#2)Comparision Operator:- If we have to compare two numbers,strings,list,dictionaries. Then use this Comparision operator, these are :- <,>,<=,>=,!=
# Result Of Comparision Operator will be "TRUE" or "FALSE" always
"""( == )Equal to Equal to Operator comapre the values of two variables"""
"""( != )Is not Equal to operator:- If numbers are not equal then printing "TRUE" but if numbers are equal printing "FALSE" """
num1 = 400
num2 = 400
print(num1 == num2)

num1 = 500
num2 = 200
print(num1 == num2)#FALSE
print(num1 > num2)#TRUE
print(num1 < num2)#FALSE"""
print(num1 != num2)#TRUE

#3)Identity Operator:- (is,is not)
##As we know in Python programming two("IMMUTABLE") integres values having same "value" then python will assign same "memory allocation". But in case of MUTTABLE Datatype it can add or change value so will have different "Memory Allocations"
num1 = 200
num2 = 200
print(num1 == num2)#TRUE
print(num1 is num2)#TRUE
num1 = 200
num2 = 100
print(num1 == num2)#FALSE
print(num1 is not num2)#TRUE
"""But in case of list or any other function"""
l = [10,20,30]
l2 = [10,20,30]
print(l == l2)#TRUE
print(l is l2)#FALSE
"""Here in case of list by comparision operator it's showing "TRUE" but by identity operator it's showing "FALSE" because... """
# Equal to Equal to Operator( == ) or Comparision Operator compare the "Values" while identity operator( is,isnot ) compare the "MEMORY ALLOCATION" and since "list" is "MUTTABLE DATATYPE" which stores different values at different memorry allocation that's it's showing "FALSE"
print(l is not l2)#TRUE

#4)Assignment Operator:- (=,+=,-=,*=,/=)
"""(=) Equal to operator alwas assign the value written at R.H.S """
num1 = 100
num1+=5 #or num1 = num1+5
print(num1)
num2 = 100
num2-=5 #or num2 = num2-5 
print(num2)

#5)Bitwise Operator:- (&,|,^,>>,>>)
num1 = 2
num2 = 1
print(bin(num1))#0b10
print(bin(num2))#0b1
print(bin(num1),bin(num2))#0b10 0b1
print(num1 & num2)#0
print(num1 | num2)#3
print(2 >> 1)#1 ( Shifted in binary at R.H.S )

#6)Logical Operators:- (and.or.not)
""""AND" operator will write and "TRUE" when both the operations are "TRUE" only
"oR" Operator will write "TRUE" if any of both operation is "TRUE"
"NOT" is the opposite of result of any operation if result is "TRUE" then it will show "False" similarly if result is "FALSE" it will show "TRUE"
"""
print(10==15 and 20==20)#False
print(10==10 and 20==20)#True
print(10==15 or 20==20)#True
print(not(10==10))#False
print(not(20==15))#True

#7)Membership operator:- (in,notin)
# Uses for getting infor of any element or data that it is available in this or not
l = [10,100,200,300,400]
print(100 in l) #True
print(500 in l) #False
print(500 not in l) #True

s = "Shubham is learning Artificial Intellegence"
print("Artificial" in s) #True
print("artiFicial" in s) #False ( So keep remener that it's CASE SENSITIVE )










 














