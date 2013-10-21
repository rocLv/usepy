#coding=utf-8
import io
import time
import csv

f = open("D:\Downloads\shifenzheng.csv\\badfile.txt",'r')
#f2 = open("D:\Downloads\shifenzheng.csv\shifenzheng.csv",'rU')

str1 ='123,,,ID,310222197707072130,M,19770707,-,-,,,CHN,-1,-1,,,,,,13761100450,-,-,jjcs8@163.com,,,,,,,,,,680'
str2 ='顾坚正,,,ID,310109195701013639,M,19570101,上海市,,F,ASI,CHN,31,310109,,,,,,13917970209,,,,汉,早餐,上网,高楼层客房,远离电梯的客房,,,,,,0,2012-8-18 1:50:04,896'
str_h = 'Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id'

print len(str_h.split(','))
print len(str2.split(','))

s1 = str_h.split(',')
s2 = str2.split(',')
dic = dict(zip(s1,s2))
#for k,v in dic.items():
#    print k,':',v.decode('utf-8')

for w in s1:
    print w,':',dic[w].decode('utf-8')


f3 = open("D:\Downloads\shifenzheng.csv\\f3.txt",'w+')
i =0
for line in f:
    line = line[line.find(',')+1:]
    print line
    #i += 1
    #assert i !=10,'stop'
    f3.writelines(line)

f.close()
f3.close()
#while True:
#    line = f.readline()
#    print line
#    if not line :
#        break
#    time.sleep(1)
