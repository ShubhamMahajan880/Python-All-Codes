# Regular Expression Modules in Python programming language :- 
import re

# For importing this moduel we have to learn about some """METACHARACTERS"""

#. - any char
#[a-z A-Z] - char class a or b or c ... or z A or B or C .... or Z
#[0-9] - digit class 0 or 1 or 2 ..... or 9
#
#+ - atleast one [a-z]+
#* - Zero or More
#
#^ - Start of the string ( Caret or Circumflex )
#$ - End of the String
#
#? - Optional
#
#[a-z]{2,4} ( It will, print minimum of 2 & maximum of 4 characters )
#s

""" A example for applicability of RE Module:-"""
# Ex.-1) check for any particular PAN NO. that it's valid or not



s = "GWNPM4648K"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]") #with [A-Z], there is no any curely bracket then by default it has acess of only 1 element 
l = re.findall(r,s) # (r - indicates for reagular expression, while s - indicates for which we have to check )
print(l) #['GWNPM4648K']
# ( if the expression is valid then it will print the result otherwise not )



s = "GWNPM46485555K"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l) #[] shows FALSE by incicating empty brackets when RE Module is not matched

""" in the case when :- """

s = "AAAAAAGWNPM4648K"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l)# ['GWNPM4648K'] Still this is printing this correct PAN No. by taking initial 5 characters with further pattern, to avoding this we can use here "STARTING OF STRING META OPERATOR" )



s = "AAAAAAGWNPM4648K"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l) # []


s = "GWNPM4648KZZZZZZZZ"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l)#['GWNPM4648K'] Still this is printing this correct PAN No. by taking initial  characters with  pattern, to avoding this we can use here "ENDING OF STRING META OPERATOR" )

s = "GWNPM4648KZZZZZZZZ"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)#[]

s = "AAAAAGWNPM4648K555555"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)#[]

#Ex.2 - cHECK for any contact number that it's valid or not:-

s = "9669999880"
r = re.compile("[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)# ['9669999880']

s = "55559669999880"
r = re.compile("[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)#['9669999880']( For Avoiding this mistakes and getting the actual number use "INITIAL STRING CHARACTER"

s = "55559669999880"
r = re.compile("^[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)#[]

s = "96699998809999999"
r = re.compile("[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)#['9669999880'] ( Fot this case use "END STRING CHARACTETR )

s = "96699998809999999"
r = re.compile("[6-9][0-9]{9}$")
l = re.findall(r,s)
print(l)


#Ex.3 - check for the correct pattern of date by RE Module concept from pyton progtramming language
"""dd-mm-yyyy"""
s = "26-06-2002"
r = re.compile("^[0-9]{2}-[0-1][0-9]-[0-9]{4}$")
l = re.findall(r,s)
print(l)# ['26-06-2002']

s = "11126-05466-2002565"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)#[]














































































