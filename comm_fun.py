#coding=utf-8
"Common functions"

import os
import string
import sys


# Create directory witch name end with numbers,when the directory had existed.
# return: the path
# eg: 
# existed: mydir,mydir1,mydir4
# expext: mydir
# resualt:  mydir2
def makedir(basepath,newdir='newfolder'):
    if str.strip(basepath) == '':
        raise ValueError
    basepath = os.path.normcase(basepath)
    p = basepath + os.sep + newdir
    if not os.path.exists(p):
        os.makedirs(p)
        return p 
    
    dlist = os.listdir(basepath)
    i = 1
    #k = 1
    name = newdir + '1'
    while True:
        nlist = []
        name = newdir + str(i)
        found = False
        for e in dlist:
            if os.path.isfile(e):
                continue
            if e.startswith(name[0:-1]):
                nlist.append(e)
                if e == name:
                    found = True
                    i += 1
                    name= newdir + str(i)

        if not found:
            break
        else:
            dlist = nlist

        ## It can't be a dead loop
        #k += 1
        #if k >= sys.maxint :
        #    return Exception

    os.makedirs(basepath + os.sep + name)
    return basepath + os.sep + name
# end function 

# get file name with file-name endwith numbers 
# eg: myfile2.txt myfile3.txt
def makefile(basepath,fname='unspecitiedfilename',withextend=True):
    if str.strip(basepath) == '':
        raise ValueError
    basepath = os.path.normcase(basepath)
    dlist = os.listdir(basepath)
    i = 1
    #k = 1
    fn = ''
    if withextend:
        if fname.rfind('.') == -1:
            fn = fname
        else:
            fn = fname[0:fname.rfind('.')]
    else:
        fn = fname

    fext = fname[fname.rfind('.'):]

    name = fn + '1'
    if withextend:
        name += fext
    while True:
        nlist = []
        name = fn + str(i)
        if withextend:
            name += fext
        found = False
        for e in dlist:
            if os.path.isdir(e):
                continue
            if e.startswith(name[0:-1]):
                nlist.append(e)
                if e == name:
                    found = True
                    i += 1
                    name= fn + str(i) 
                    if withextend:
                        name += fext

        if not found:
            break
        else:
            dlist = nlist

        ## It can't be a dead loop
        #k += 1
        #if k >= sys.maxint :
        #    return Exception

    return basepath + os.sep + name
# end function 



