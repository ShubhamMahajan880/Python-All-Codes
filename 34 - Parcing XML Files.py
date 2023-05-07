#parsing XML files using xmltodict in python Programming Language:-
import xmltodict
handle = open("xml_input.xml","r")
content = handle.read()
print(content)
"""
<Result success = "false">
    <message>Cannot open remote file '/home/user/examplefile.txt'.</Message>
    <ErrorCode> 2 </Errorcode>
    <RequestCode> 3 </RequestCode>
</Result>
# Now have a look that how we can pass this file using python
"""

d = xmltodict.parse(content)
print(d)
print(d['Result'])
