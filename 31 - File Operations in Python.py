# Getting Started with File Operation in Python Programmig Language
#r => read
#r+
#w=> write
#w+
#a=>append
#a+


fp = open("input.txt","r") #name of text file,the mode in which we want to open ths file
content = fp.read() # this read function always return in terms of string 
print(content)

"""
Scholarship Notes

TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022

Protean e-Gov Renewal Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)
Publish Date : 15-03-20


Protean e-Gov Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)


Pragati Scholarship Programme For Girls Students pursuing Under Graduate Course


Arvind Fashions Limited ITI Scholarship Scheme 2021-2022
Publish Date : 24-02-2022

Arvind Fashions Limited UG Scholarship Scheme 2021-2022


Sandvik Coromant Girls Scholarship Program (21-22)

AIA Scholarship Programme For Undergraduate Course

AIA Scholarship Programme For B.E/B.Tech Course


Astral Foundation Scholarship For Undergraduate Courses (2021-2022)


Astral Foundation Scholarship For B.E/B.Tech Course (2021-2022)
Publish Date : 28-02-2022


Astral Foundation Renewal Scholarship For Under Graduate Course (2021-2022)


Astral Foundation Renewal Scholarship For B.E/B.Tech Course (2021-2022)


Timken Scholarship for B.E./B.Tech Students (2021-2022)

Timken Renewal Scholarship for B.E./B.Tech Students (2021-2022)

H.G. Infra Engineering Ltd. Scholarship for Undergraduate Courses

H.G. Infra Engineering Ltd. Scholarship for B.E./B.Tech Course


2 years programme:-
18000 only recorded
22000 live+recorded

1 year programme:-
Recorded 6-7 month-11000
+ live:- 16000
12 month:- 22000
"""
print("_______________")
content = fp.read()
print(content)


"""
_______________
	Scholarship Notes

TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022

Protean e-Gov Renewal Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)
Publish Date : 15-03-20


Protean e-Gov Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)


Pragati Scholarship Programme For Girls Students pursuing Under Graduate Course


Arvind Fashions Limited ITI Scholarship Scheme 2021-2022
Publish Date : 24-02-2022

Arvind Fashions Limited UG Scholarship Scheme 2021-2022


Sandvik Coromant Girls Scholarship Program (21-22)

AIA Scholarship Programme For Undergraduate Course

AIA Scholarship Programme For B.E/B.Tech Course


Astral Foundation Scholarship For Undergraduate Courses (2021-2022)


Astral Foundation Scholarship For B.E/B.Tech Course (2021-2022)
Publish Date : 28-02-2022


Astral Foundation Renewal Scholarship For Under Graduate Course (2021-2022)


Astral Foundation Renewal Scholarship For B.E/B.Tech Course (2021-2022)


Timken Scholarship for B.E./B.Tech Students (2021-2022)

Timken Renewal Scholarship for B.E./B.Tech Students (2021-2022)

H.G. Infra Engineering Ltd. Scholarship for Undergraduate Courses

H.G. Infra Engineering Ltd. Scholarship for B.E./B.Tech Course


2 years programme:-
18000 only recorded
22000 live+recorded

1 year programme:-
Recorded 6-7 month-11000
+ live:- 16000
12 month:- 22000
"""

content = fp.read(45)
print(content)
"""
	Scholarship Notes

TSS Sameer Aatmanirbhar s
"""

content  = fp.readlines() # in case of read command it prints the content in terms of "string" while in case of readlines it writens in terms of "LIST"
print(content)
print(type(content))# <class 'list'> 
"""
['\tScholarship Notes\n', '\n', 'TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022\n', '\n', 'Protean e-Gov Renewal Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)\n', 'Publish Date : 15-03-20\n', '\n', '\n', 'Protean e-Gov Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)\n', '\n', '\n', 'Pragati Scholarship Programme For Girls Students pursuing Under Graduate Course\n', '\n', '\n', 'Arvind Fashions Limited ITI Scholarship Scheme 2021-2022\n', 'Publish Date : 24-02-2022\n', '\n', 'Arvind Fashions Limited UG Scholarship Scheme 2021-2022\n', '\n', '\n', 'Sandvik Coromant Girls Scholarship Program (21-22)\n', '\n', 'AIA Scholarship Programme For Undergraduate Course\n', '\n', 'AIA Scholarship Programme For B.E/B.Tech Course\n', '\n', '\n', 'Astral Foundation Scholarship For Undergraduate Courses (2021-2022)\n', '\n', '\n', 'Astral Foundation Scholarship For B.E/B.Tech Course (2021-2022)\n', 'Publish Date : 28-02-2022\n', '\n', '\n', 'Astral Foundation Renewal Scholarship For Under Graduate Course (2021-2022)\n', '\n', '\n', 'Astral Foundation Renewal Scholarship For B.E/B.Tech Course (2021-2022)\n', '\n', '\n', 'Timken Scholarship for B.E./B.Tech Students (2021-2022)\n', '\n', 'Timken Renewal Scholarship for B.E./B.Tech Students (2021-2022)\n', '\n', 'H.G. Infra Engineering Ltd. Scholarship for Undergraduate Courses\n', '\n', 'H.G. Infra Engineering Ltd. Scholarship for B.E./B.Tech Course\n', '\n', '\n', '2 years programme:-\n', '18000 only recorded\n', '22000 live+recorded\n', '\n', '1 year programme:-\n', 'Recorded 6-7 month-11000\n', '+ live:- 16000\n', '12 month:- 22000\n', '\n', '\n', '\n', '\n', '\n', '\n']
"""
content = fp.readlines()
print(content[:5]) # Slicing operation ( i eant to print initial first five lines only )
"""
['\tScholarship Notes\n', '\n', 'TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022\n', '\n', 'Protean e-Gov Renewal Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)\n']
""" # So here by usig slicing operation it's printing onlr initial 5 lines
# So readlines will return the list and every line will be an element in the list not on the basis of fullstop while on the basis of new line )
# and python is making new line as an element on the basis of next line and shown as \n'

content = fp.readline() #by using only readline command only we can print the first line only, again not on the basis of fullstop while on the basis of a new line
print(content) 
"""
	Scholarship Notes """
	
content = fp.readline()#On use further it will start printing from next line
print(content)
"""
	Scholarship Notes



TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022
"""
content = fp.readline() # So by using this readline command agaian and again according to condition we can print next line further
print(content)
"""
	Scholarship Notes



TSS Sameer Aatmanirbhar scholarship for Under Graduate 2021-2022



Protean e-Gov Renewal Scholarship Scheme for students pursuing B.E/B.Tech (2021-2022)
"""

for x in fp:
    print(x)
    





























