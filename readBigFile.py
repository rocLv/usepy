# -*- coding=utf-8 -*-
'''
2013/10/17
解析某酒店泄露的数据,大约2KW记录
从CSV文件导入到MySQL
'''
import io
import MySQLdb
import time

file=open("D:\Downloads\shifenzheng.csv\shifenzheng.csv",'r')
badfile=open("D:\Downloads\shifenzheng.csv\\badfile.txt",'w+')
#file=codecs.open("D:\Downloads\shifenzheng.csv\shifenzheng.csv",'r','utf-8')
sql = 'insert into shifenzheng (Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
#sql2 = ' insert into test (id,name,gender) values (%s,%s,%s)'
lines = file.readline()
lst = list()
bad = list()
sum =0
sum_ex=0.0
exit_flag=0
db = MySQLdb.connect(host='localhost',db='shifenzheng',user='root',passwd='root',charset='utf8')
cursor = db.cursor()

#print cursor.execute('truncate table shifenzheng;')

time.clock()
try:
    while True:
        lines = file.readlines(50000)
        if not lines:
            print '\n >>>>>>> not lines!!!!!'
            print 'readline() : ',file.readline()
            exit_flag += 1
            if exit_flag >=10:
                break
        for ln in lines:
            l = ln[0:-1].split(',')
            if len(l) ==33:
                lst.append(l)
            else:
                bad.append(str(len(l))+','+ln)
                sum_ex += 1
            #print cursor.execute(sql,l.split(','))
        sum += len(lst)
        print cursor.executemany(sql,lst)
        db.commit()
        lst =[]
        msg = 'take times(m):%3f ,legal data: %d , bad data:%d , %5f%% \n' %(time.clock()/60,sum,sum_ex,sum_ex/sum*100)
        print msg
        if len(bad) >=1000:
            badfile.writelines(bad)
            #badfile.writelines(msg)
            bad=[]


    badfile.writelines(bad)
    badfile.writelines('\n end!')
    print 'total insert lines:',sum
    print 'total times:',time.clock()/60
except Exception,ex:
    print ex


#sql2 = 'select * from test'
#cursor.execute(sql2)
#result = cursor.fetchall()
#for r in result:
#    print r

file.close()
badfile.close()
cursor.close()
db.close()


#try:
#    #db = MySQLdb.connect(host='localhost',db='shifenzheng',user='root',passwd='root')
#    db = MySQLdb.connect(host='localhost',db='dh_database',user='root',passwd='root')
#except Exception,e:
#    print e
#cursor = db.cursor()
##sql = 'select * from shifenzheng'
#sql = 'select * from co_data_raw limit 100'
#cursor.execute(sql)
#
#data = cursor.fetchone()
##data=cursor.fetchall()
#for d in data:
#    print d
#
#
#cursor.close()
#db.close()


