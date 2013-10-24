#coding=utf-8
import io
import time
import csv
import MySQLdb

f = open("d:/xxoo.csv",'rU')

for line in f:
    if not f :
        break
    #print line.decode('utf8')
    print line.split(',')
    time.sleep(0.1)
