import re

line = "cats are smarter tha dogs"

matchobj = re.search(r'(.*)cats(\.*)',line,re.M|re.I)

if matchobj:
    print ("matchobj.group():", matchobj.group())
    print ("matchobj.group():", matchobj.group(1))
    print ("matchobj.group():", matchobj.group(2))
