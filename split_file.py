# Split text file to small piece

import os

def split_file(sourceFile,pieceSize):
    print "Start spliting file: " + sourceFile
    print "filesize: "+ str(os.path.getsize(file))
    
    count =1
    index = 1
    tmpfile = os.path.splitext(file)[0] + "_split_" + str(index) + os.path.splitext(file)[1]
    newfile=False
    fobj = open(tmpfile,"w+")
    f = open(sourceFile)
    for eacheline in f:
        if count % 1000 == 0 : # Every 1000 times check file size
            if os.path.getsize(tmpfile) >= pieceSize: 
                fobj.close()
                index += 1
                tmpfile = os.path.splitext(file)[0] + "_split_" + str(index) + os.path.splitext(file)[1]
                fobj = open(tmpfile,"w+")
                print "New piece has been created :" + tmpfile 
        fobj.write('%s' % eacheline)
        count += 1

    fobj.close()
    f.close()

    print "Processing complete."



pieceSize  = 100 * 1024*1024
file ="D:\Database - 0318\log\AppErr.log"
info = raw_input(" Start split file ?( Y/N)")
info = info.strip().lower()
#tmpfile = os.path.split(file)[0] +"\\"+ os.path.split(file)[1]+ "_split_" + str(1) + os.path.splitext(file)[1]
#tmpfile = os.path.split(file)[0] +"\\"+ os.path.basename(file) + "_split_" + str(1) + os.path.splitext(file)[1]
#print os.path.splitext(file)

if info == "y":
    split_file(file,pieceSize)



