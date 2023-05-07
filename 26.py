import re

s = "26-06-2002"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
#l = re.findall(r,s)
#print(l)# ['26-06-2002']

# Search Method :- There is a search method for identify that it's correct pattern or not
""" Search method try to search for entered particular pattern in the string if pattern exist correctly it indicates "MATCH OBJECT" &
if pattern does not exist it returns me "NONE" """

m = re.search(r,s)
print(m)# <re.Match object; span=(0, 10), match='26-06-2002'>

s = "26-06-20025"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
m = re.search(r,s)
print(m)# None

# Group:-if we want to fetch the value of string then there is a method called as "GROUP"
s = "26-06-2002"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
m = re.search(r,s)
print(m.group())#26-06-2002 ( Value of wanted String )

s = "26-06-200"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
m = re.search(r,s)
#print(m.group())#AttributeError: 'NoneType' object has no attribute 'group'

""" Group by if & else concpets:- """
m = re.search(r,s)
if m:
    print(m.group())
else:
    print("Pattern Not found")
""" For extract data from the matched data so that we can perform operation on the string we can use group, for this insert parethesis in data for
different different groups"""
s = "26-06-2002"
r = re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")

m = re.search(r,s)
if m:
    print(m.group())
else:
    print("Pattern Not found")
# Output in different cases - print(m.group())  26-06-2002
#                             print(m.group(0)) 26-06-2002
#       For Date index is (1) print(m.group(1)) 26
#       For Month index is 2) print(m.group(2)) 06
#       For Year index is (3) print(m.group(3)) 2002
#       If index is (4)       print(m.group(4)) IndexError: no such group

                              
""" If we do not want to do with indexing we can also metioned as name :- """
# Name Group:- The group concept in which at the place of index we use names is called as "Name gROUPS" 

s = "26-06-2002"
r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")

m = re.search(r,s)
if m:
    print(m.group("date"))
else:
    print("Pattern Not found")


# Output in different cases - print(m.group("date"))  26
#                             print(m.group("month")) 06
#                             print(m.group("year"))  2002


# Capturing & Non-Capturing Groups:-
s = "+91 9826410840"
r = re.compile("(?:\+91\s)?([6-9][0-9]{9})") # "?" is used for additional (Here +91 is additional that's why ) & "\s" uses for space between the additional group and number

m = re.search(r,s)
if m:
    print(m.group())
else:
    print("Pattern not found")
    
#+91 9826410840
     
""" Some Meta Character Concepts:-

For [0-9] we can use - \d
For [^0-9]           - \D
For [a-z, A-Z, 0-9]  - \w
Other than this use it's complement - \W
For Space - \s
Other than Space - \S


































    


