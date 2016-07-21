#function module
"function module"

def fun(txt):
    print 'function module output:'+txt

if __name__ == "__main__":
    print "Function module self running"
else:
    print "Function module import running"
    print "Function module name:"+__name__
