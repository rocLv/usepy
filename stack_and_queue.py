#coding=utf-8

# stack AND queue
a=[]
i=0
while(i<10):
    a.append(i+1)
    i+=1

print a

while(len(a) >0):
    print a.pop()
    print a

print "now:"
print a

print " queue"
i=0
while(i<10):
    a.append(i+1)
    i+=1

while(len(a)>0):
    print a.pop(0)
    print a




