#Parcing JSON Files Using Python Programming Language :- (How to create a json file, read update and modify)
"""json objects      dict {"key":"value"}
numbers 10 10.55  int float
array [10,"string"] list
                    tuple
" "                 ' '  "" """ """
"""
import json

handle = open("json_input.json","r")
content = handle.read()

print(content)

"""
{
    "database":{
        "host": "localhost",
        "port" : 3310,
        "user" : "root",
        "password" : "12345"
       },
    "files" : {
        "log" : "/log/app.log",
        "errorLog" : "/log/error.log"
     }
}

"""
d = json.loads(content)
print(d)# is the command by which we get the data in dictionary format 
"""
{'database': {'host': 'localhost', 'port': 3310, 'user': 'root', 'password': '12345'}, 'files': {'log': '/log/app.log', 'errorLog': '/log/error.log'}}
"""
print(d['database'])# For get the valueplair inside the key
"""
{'host': 'localhost', 'port': 3310, 'user': 'root', 'password': '12345'}
"""
print(d['database']['port'])#3310
# If i want to modify the value inside the dictionary for such files
d['database']['port'] = 3330
print(d)
"""
{'database': {'host': 'localhost', 'port': 3330, 'user': 'root',
'password': '12345'}, 'files': {'log': '/log/app.log',
'errorLog': '/log/error.log'}}
"""
# Modifying values in terms of tuple :
print(d['files']['log'])
d['files']['log'] = ("/log/app.log","/log/mysql/app.log")
print(d)
"""
{'database': {'host': 'localhost', 'port': 3330, 'user': 'root',
'password': '12345'}, 'files': {'log': ('/log/app.log', '/log/mysql/app.log'),
'errorLog': '/log/error.log'}}
"""
j = json.dumps(d,indent = 4,sort_keys = True)
print(j)
"""
{"database": {"host": "localhost", "port": 3330, "user": "root",
"password": "12345"}, "files": {"log": ["/log/app.log", "/log/mysql/app.log"],
"errorLog": "/log/error.log"}}
"""
handle = open("json_output.josn","w")
handle.write(j)
"""
{"database": {"host": "localhost", "port": 3330, "user": "root",
"password": "12345"}, "files": {"log": ["/log/app.log", "/log/mysql/app.log"],
"errorLog": "/log/error.log"}}
"""
handle.close()
#j = json.dumps(d,indent = 4) ( by using this command i can get indented json file )
"""
{
    "database": {
        "host": "localhost",
        "port": 3330,
        "user": "root",
        "password": "12345"
    },
    "files": {
        "log": [
            "/log/app.log",
            "/log/mysql/app.log"
        ],
        "errorLog": "/log/error.log"
    }
"""    
#j = json.dumps(d,indent = 4,sort_keys = True) [ it's a command by which we can gey sorted value pairs in json files )
{
    "database": {
        "host": "localhost",
        "password": "12345",
        "port": 3330,
        "user": "root"
    },
    "files": {
        "errorLog": "/log/error.log",
        "log": [
            "/log/app.log",
            "/log/mysql/app.log"
        ]
    }

"""








































































