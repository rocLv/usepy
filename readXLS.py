# -*- coding:utf-8 -*-
from mmap import mmap, ACCESS_READ
from xlrd import open_workbook

fname = 'c:\ss.xls'
fname = 'D:\VSS\NCardWebSys\WebNCard\Languages\界面待翻译.xls'
f2 = 'd:\\vss\NCardWebSys\WebNCard\Languages\Chinese_zh_CN.xml'

# print open_workbook(unicode(fname,'utf8'))
#f = open(f2, 'r')
#line = f.readline()
# while(line):
#    print line
#    line = f.readline()

wb = open_workbook(unicode(fname, 'utf8'))
for s in wb.sheets():
    print 'Sheet:', s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col))
         v=str(values[1])
         print v
    print 'end'
