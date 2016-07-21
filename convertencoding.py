# coding:utf-8
#!/usr/bin/python

import os
import sys

# var
ignoreFile = []
ignoreDir = []
validExtend =['.java','.xml','.property','.properties','.txt']


def convert(filename, in_enc="GBK", out_enc="UTF-8"):
    print 'convert %s -> %s %s' % (in_enc, out_enc, filename),
    fp = open(filename)
    content = fp.read()
    fp.close()
    # convert the concent
    try:
        new_content = content.decode(in_enc).encode(out_enc)
        # write to file
        fp = open(filename, 'w')
        fp.write(new_content)
        fp.close()
        print '   DONE'
    except:
        print "   ERROR"


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file[0] == '.':
                continue

            if file in ignoreFile:
                continue

            tmp = os.path.splitext(file)
            if len(tem)=2 and tmp not in validExtend:
            	continue

            path = os.path.join(root, file)
            convert(path)
    print " done"


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            convert(path)
        elif os.path.isdir(path):
            explore(path)
    else:
        print 'please input filename OR directory'

if __name__ == "__main__":
    str = 'ab.exe'
    print os.path.splitext(str)
