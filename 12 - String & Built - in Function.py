#Str Datatypes buit-in functions:-
#Use of format
num1 = 200
num2 = 500
print("Value of num1 is:- ",num1,"And the value of num2 is:- ",num2)
print("value of num1 is - {} and the value of num2 is - {}".format(num1,num2))#value of num1 is - 200 and num2 is 500
print("value of num1 is - {0} and num2 is {1}".format(num1,num2))#value of num1 is - 200 and num2 is 500
#There is indexing for both the values for first value indexing is (0) and for second value indexing is (1)
print("value of num1 is - {1} and num2 is {0}".format(num1,num2))#value of num1 is - 500 and num2 is 200
#it has just reversed the values duw to reverse the indexing
print("value of num1 is:- {val1} and the value of num2 is:- {val2}".format(val1=num1,val2=num2))#value of num1 is:- 200 and the value of num2 is:- 500


s = "python sample string"
print(s)#python sample strin    
print(id(s))#52795072
s = s.capitalize()
print(s)#Python sample string
print(id(s))#52852736
#So we are assigning the same variable name but internally stored at different memory location because strings are immutable
print(s.upper())#PYTHON SAMPLE STRING
print(s.lower())#python sample string
print(s.title())#Python Sample String


#Buit in functions in python programming:-
#it gives the output in terms of "TRUE" ot "FALSE"
#Standard Fomat may be expressed as - print(variable.istask())
s = "python sample string"
print(s.isupper())#False
s = s.upper() 
print(s.isupper())#True
print(s.islower())#False
s = s.lower()
print(s.islower())#True
print(s.istitle())#False
s = s.title()
print(s.istitle())#True

#Spli & Join function in Pyhton programming:-
s = "HTML,CSS,PYTHON,JAVA,JAVASCRIPT,DJANGO"
l = s.split(",")
print(l)#['HTML', 'CSS', 'PYTHON', 'JAVA', 'JAVASCRIPT', 'DJANGO']
l = s.split(" ")
print(l)#['HTML,CSS,PYTHON,JAVA,JAVASCRIPT,DJANGO']
s1 = (" ").join(l)
print(s1)

#Use of Maketrans and Translate Function:-
s1 = "abcd"
s2 = "1234"
s3 = "Python Sample String abcd"
table = str.maketrans(s1,s2)
result = s3.translate(table)
print(result)#Python S1mple String 1234z

#find,index and rfind function:- 
s = "HTML,CSS,PYTHON"
print("PYTHON" in s)#True
print(s.index("PYTHON"))#9
# it is case sensitive, if i write python at the place of PYTHON it showsme some error
#in case of multiple occurance of PYTHON it will count indexing for first one and return
s = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))#9
#find also start indexxing from left to right
print(s.find("PYTHON"))#9
#but in case of case sensitiveness, it will shows -1
print(s.find("python"))#-1
# This is the only difference betwen find and index functions that in case of(case sensitivenss) in index function it shoes "ERROR" but in find it shoes "-1".
s = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print("PYTHON" in s)
print(s.rfind("PYTHON"))#23
#r.find also uses for indexing but start from Right to Left


#USe of Strip Function:-
#it is uses for removing spacing inside the string or any other special character inside the string
s = "         This is sample string               "
s1 = s.strip(" ")
print(s1)#This is sample string
s = "*******************This is sample string*********"
s1 = s.strip("*")
print(s1)#This is sample string
s1 = s.lstrip("*")
print(s1)#This is sample string*********
#lstrip is uses for removing the space,star or any special character from left hand side and similarly for Right Hand Side rstrip
s1 = s.rstrip("*")
print(s1)#*******************This is sample string


#Center and Left Right Moving Sting with Special Charcater or Space Functions
s = "python"
s1 = s.center(20,"*")
print(s1)#*******python******* ( by uing center we can print string word in center and apply selected special character and space around left & right)
s1 = s.ljust(20,"*")
print(s1)#python************** ( by uing ljust we can print string word in Left hand side )
s1 = s.rjust(20,"*")
print(s1)#**************python ( by uing rjust we can print string word in Right hand side )
s1 = s.center(100,"#")
print(s1)################################################python###############################################

#Replace Function:-
s = "html,css,python,java,html"
s1 = s.replace("html","HTML5")
print(s1)#HTML5,css,python,java,HTML5
s1 = s.replace("java","JAVASCRIPT")
print(s1)#html,css,python,JAVASCRIPT,html

print(dir(str))
help(str)

































