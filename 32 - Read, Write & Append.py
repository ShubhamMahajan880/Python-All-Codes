# File Operation:- Read,Write and Appnd
fp = open("input2.txt","w") # so in write mode even the file is not exist in particular directory then python will create the file by given name and we write in it.
fp.write("sample text line 1") #i am here specially for learning python ( in this command we write the statement which we want to metion in above named file )
"""content = fp.read()
print(content)"""#UnsupportedOperation: not readable
# So in the write mode i can only perform "WRITE" operation cannot be perfomed "READ" operaation
# & it's similar for rad mode also in "READ" mode i can only perform read operation and cannot perform "WRITE" operation
# So for avoidind such errors we have "w+" mode which stands for "WRITE as well as "READ" and "r+" mode which also stand for "READ" as well as "WRITE"
""" w+ = write + Read
    r+ = read + wrire
"""   
fp = open("input2.txt","w+")
fp.write("sample text line 1")
content = fp.read()
print(content) # this time it's not showig any error but also not printing content
# Here before writing anything in the file after creating the file, file pointer was at initial possition, then by using wrting command it reached at last possition and now it's ready for read the file that's why not showing any error
# That's why we use here two functions:- tell & seek
""" tell - uses for showing current fp possition
& seek - to change the fp possition
So, use of these both functions:- """
fp = open("input2.txt","w+")
print(fp.tell())# 0 ( initially, mouse pointer is present at initial location and ready to write,as the file created currently )
fp.write("Sample text line 1")
print(fp.tell())# 18 ( now,after writing the statement mouse pointer has reached on 18nth possition )
content = fp.read()
print(fp.tell())# 18 ( After, reading the satement mouse pointer at 18nth possition )
print(content)
""" seek function have two arguements:- (Offset,Position)
offset - indicates number of char
positin - 0 ==> Start of the file
          1 ==> Current Possition
          2 ==> End of the file
if seek(15,0) ==> having meaning change the fp(file pointer's possition) by 15 char from  start of the file
seek(0,2) ==> change the fp(filepointer's possition) by0 char from end of the file
seek(15,1) & seek(15,2) are invalid
"""
fp = open("input2.txt","w+")
print(fp.tell())# 0 ( initial possitionof muouse pointer )
fp.write("Sample text line 1")
print(fp.tell())# 18 ( after write mouse pointer locality )
fp.seek(0,0)
print(fp.tell())# 0 ( after using seek funtion the location of mouse pointer has been chnaged
content = fp.read()
print(fp.tell())# 18
print(content)# Sample text line 1 ( and now it's able to read the content in write file )

# Similar approch in case of read (r+ = read + write)
fp = open("input.txt","r+")
content = fp.read()
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
"""# now it was about reading of the file by using r+ we can write something in this read file
fp = open("input.txt","r+")
content = fp.read()
print(content)
fp.write("\n\nSample line added using python script")
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








Sample line added using python script """
# So i am able to write in the file after read

""" a ( append )
    a+( append + )
"""
# difference betwen r,r+ & w,w+ & a,a+
""" so r,r+,w,w+ ==> whenever we open the file the file pointers(fp)'s location at start
       a,a+ ==> the file pointer possition is defaultly at end
"""
fp = open("input.txt","r+")
print(fp.tell())#0 ( So, initialy the location of file pointer is at initial )
content = fp.read()
print(content)

fp = open("input.txt","a+")
print(fp.tell())# 1594 ( then, after using append+ command file posstion pointer at last of the file )
content = fp.read()
print(content)
# So, in r+ for 'READ' and in w+ for 'WRITE' first find the file pointers possition by TELL function then change it by using 'SEEK' function instead of this i can directly use "a+" method
""" difference b/w - a & - a+"""
fp = open("input.txt","a")
print(fp.tell())
content = fp.read() #UnsupportedOperation: not readable
""" but in the case of write """
fp = open("input.txt","a")
fp.write("\n\nShubham") # it automatically add the string which we want
# hence in append function we can only perform WRITE operationt NOT Read operation while in the case of a+ we can perform both "READ" as well as "WRITE" operations
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








# Shubham
"""

# ********** Summary ****************** :-

    # r => fp => start,file should already exist, read
    # r+ => fp => Start,file should already exist,read + write
    
    # w => fp => start,create a new file,write
    # w+ => fp => tart,create a new file,write + read

    # a => fp => end,create a new file, write at the end
    # a+ => fp => end,create a new file, write + read





































