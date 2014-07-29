# -*- coding:utf8 -*-
# Split File to small piece
import os

def split_file(sourceFile,pieceSize):
    print "Start spliting file: " + sourceFile
    print "filesize: "+ str(os.path.getsize(file))

    count =1
    index = 1
    tmpfile = os.path.split(sourceFile) + "_split_1." + os.path.splitext()[1]
    newfile=False
    fobj = open(tmpfile,"w+")
    f = open(sourceFile)
    for eacheline in f:
        if count % 1000 == 0 : # every 1000 times check file size
            if os.path.getsize(tmpfile) >= pieceSize: # piece size about 100m
                fobj.close()
                index += 1
                tmpfile = os.path.split(sourceFile) + "_split_" + str(index) + "."+ os.path.splitext()[1]
                fobj = open(tmpfile,"w+")
                print "New piece has been created :" + tmpfile
        fobj.write('%s' % eacheline)
        count += 1

    fobj.close()
    f.close()

    print "Processing complete."



print 'hello'
str = unicode('中文',encoding='utf-8')
print str.encode('utf-8')


#pieceSize  = 100 * 1024*1024
#file ="D:\Database - 0318\log\AppErr.log"
#info = raw_input(" Start split file ?( Y/N)")
#info = info.strip(info).lower()
#if info == "y":
#    split_file(file,pieceSize)
#


