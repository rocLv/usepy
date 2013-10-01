#main.py
"main module"
import re
import os
import string


#a = "%x" % 17
#print a
#
#str = "abcdef"
#print str.upper()
#print str.rjust(9)
#print str.zfill(9)

str = "abcdef"

m=re.match('\w',str)
print re.findall('\w',str)
#print m.group()

str = ['a.abc.com','abc.com','bb23.abc.com']
for s in str:
    m=re.match('\w*\.*abc.com',s)
    print m.group()

import comm_fun
print comm_fun.makefile('c:\\abc','test.',False)

print comm_fun.makefile('c:\\abc','test.',True)


#for (i,t) in enumerate(str):
#    print (i,t)
#
#for item in str:
#    print item
#
#for index in  range(len(str)):
#    print str[index]
#
  
if __name__ == "__main__":
    print "--->>> Main module self running"
else:
    print "--->>> Main module import running"
