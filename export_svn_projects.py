#### -*- coding:utf-8 -*-
#coding=utf-8

import os
import comm_fun

cmdstr ='svn export {0} {1}'

def exp(srcpath,dstpath):
    if os.path.isfile(srcpath):
        return None

    issvnfolder = False
    for f in os.listdir(srcpath):
        if f == '.svn' :
            issvnfolder = True
            break

    if issvnfolder :
        topath = comm_fun.makedir(dstpath,os.path.basename(srcpath))
        print topath
        cmd = cmdstr.format(srcpath,topath)
        print cmd
        tmp_output = os.popen(cmd).readlines()
        print tmp_output
    else :
        raise Exception( 'The given path is not a director')



source = 'd:/allprojects/drink/doc'
destination = 'd:/desktop/svn'

source = os.path.normcase(source)
destination = os.path.normcase(destination)

print exp(source,destination)
