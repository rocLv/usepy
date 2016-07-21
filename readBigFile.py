# -*- coding=utf-8 -*-
'''
2013/10/17
解析某酒店泄露的数据,大约2KW记录
从CSV文件导入到MySQL
建表脚在文件末尾
'''
import io
import MySQLdb
import time
import re


def readBigFile():
    '''处理过程中发现CSV文件有些格式问题，比如含有分隔符的字符串未处理,
        文件中出现一些文件结束的行，导致判断文件结束时，无法只判断一次,
        把不符合格式的行暂时保存到另一份文件'''
    try:
        file = open("D:\Downloads\shifenzheng.csv\shifenzheng.csv", 'r')
        badfile = open("D:\Downloads\shifenzheng.csv\\badfile.txt", 'w+')
        # file=codecs.open("D:\Downloads\shifenzheng.csv\shifenzheng.csv",'r','utf-8')
        sql = 'insert into shifenzheng (Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
        title = file.readline()  # Read the title of CVS
        badfile.writelines(title)  # Save title to badfile
        lst = list()
        bad = list()
        sum = 0
        sum_ex = 0.0
        exit_flag = 0
        db = MySQLdb.connect(
            host='localhost', db='shifenzheng', user='root', passwd='root', charset='utf8')
        cursor = db.cursor()

        # print cursor.execute('truncate table shifenzheng;')
        time.clock()

        while True:
            lines = file.readlines(50000)
            # 故增加 if not lines 的判断次数
            if not lines:
                print '\n >>>>>>> not lines!!!!!'
                print 'readline() : ', file.readline()
                exit_flag += 1
                if exit_flag >= 10:
                    break
            for ln in lines:
                l = ln[0:-1].split(',')
                # 过滤不符合格式的行
                if len(l) == 33:
                    lst.append(l)
                else:
                    bad.append(ln)
                    sum_ex += 1
                # print cursor.execute(sql,l.split(','))
            sum += len(lst)

            # print cursor.executemany(sql,lst)
            # db.commit()

            lst = []
            msg = 'take times(m):%3f ,legal data: %d , bad data:%d , %5f%% \n' % (
                time.clock()/60, sum, sum_ex, sum_ex/sum*100)
            print msg
            if len(bad) >= 1000:
                badfile.writelines(bad)
                bad = []

        badfile.writelines(bad)
        badfile.writelines('\n end!')
        print 'total insert lines:', sum
        print 'total times:', time.clock()/60
    except Exception as ex:
        print ex
    finally:
        file.close()
        badfile.close()
        cursor.close()
        db.close()


def readBadFile():
    '''解析不符合格式的文件'''
    # CSV共33列，标题：
    """Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id
    """
    linenumber = 0
    all_list = []
    try:
        f = open("D:\Downloads\shifenzheng.csv\\f3.txt", 'rU')
        line = f.readline()
        while True:
            line = f.readline()
            linenumber += 1
            if not line:
                break
            # 获取满足一条记录数据，长度至少大于33列
            line = line[0:-1]
            lst = line.split(',')
            while len(lst) < 33:
                line = f.readline()
                linenumber += 1
                if not line:
                    break
                line = line[0:-1]
                lst.extend(line.split(','))

            # 去掉开头和结尾的 - 空格
            for k, v in enumerate(lst):
                if v.startswith('-'):
                    v = v[1:]
                if v.endswith('-'):
                    v = v[0:-1]
                lst[k] = str.strip(v)

            lst = processAddressZip(lst)

            lst = processEmailAndNumber(lst)

            lst = lastThreeMeta(lst)
            if len(lst) ==None:
                continue

            # output(lst)

            all_list.append(lst)

        # print len(all_list)
        saveToMySQL(all_list)
        # print 'lines of file:', linenumber
    except Exception as ex:
        print ex
    finally:
        f.close()


def processMultiName(lst):
    # 处理多个人名一起登记的情况
    temp = [lst[0]]
    for k in range(len(lst)):
        if str.strip(lst[k+1]) != '':
            temp[0] += ','+str.strip(lst[k+1])
        else:
            temp.extend(lst[k+1:])
            break
    lst = temp
    return lst


def processAddressZip(lst):
    # 处理地址中含有的逗号，分析地址栏后的几个字段是否为地址字段的值
    # 地址后边可能是邮政编码或门牌号，街道号等
    # 邮政编号还有 -123456 奇葩格式的,邮政编号后边的字段值为空
    temp = lst[0:8]
    for k in range(len(lst)):
        v = str.strip(lst[k+8])
        # 如果是中文或字母，则添加到地址
        if v != '' and v != '-' and not str.isdigit(v):
            temp[7] += ','+v
        # 如果是数字且是大陆的身份证号，且长度不是6位（说明不是邮政编码），则添加到地址
        elif str.isdigit(v) and len(v) < 6 and len(lst[4]) >= 15:
            temp[7] += ' '+v
        # 如果是6位数字，但是后一字段的值不是空，说明此值也是地址字段的值
        elif str.isdigit(v) and lst[k+8+1] != '':
            temp[7] += ','+v
        else:
            temp.extend(lst[k+8:])
            break
    lst = temp
    # 处理邮政编码字段值及后一字段值颠倒
    if str.isdigit(lst[9]) and lst[8] == '':
        lst[8] = lst[9]
        lst[9] = ''
    # lst[11] 是国家代码
    if len(lst) > 11 and len(lst[10]) == 3:  # 前移一位
        lst.insert(10, '')
    if len(lst) > 13 and len(lst[12]) == 3:  # 后移一位
        del lst[11]
    return lst


def processEmailAndNumber(lst):
    # 处理电话号码填写问题
    # 查找Email和手机、电话，传真 19~22
    # re_email =
    # '^([a-zA-Z0-9._-])+@([a-zA-Z0-9])+.([a-zA-Z0-9]){1,5}$'
    temp = lst
    s = ','.join(lst[18:23]).lower()
    s = s.replace(' ', ',').split(',')
    s = set(s)  # 去重复
    s = list(s)
    for k, v in enumerate(s):
        if v == '' or str.isalpha(v):
            del s[k]
    s.extend(['']*4)
    i = 0
    for k in range(4):
        temp[22] = temp[22].lower()
        if '@' in s[k]:
            if s[k] in temp[22]:
                pass
            elif temp[22] == '':
                temp[22] = s[k]
            else:
                temp[22] += ','+s[k]
        else:
            temp[19+i] = s[k]
            i += 1
    temp[17] = ''  # 电话号码前两字段都是空的
    temp[18] = ''
    lst = temp
    return lst


def output(lst):
    # 输出
    for k, v in enumerate(lst[0:34]):
        if v == '':
            v = '$'
        # v = v.decode('utf8')
        if k == 0 or k == 1 or k == 2 or k == 3:
            pass
           # print '%10s' % v.decode('utf8'),
        elif k == 4:
            print '%19s' % v,
        elif k == 7:  # address
            print '%10s' % 'address',
        elif k == 8 or k == 13:  # zip
            print '%6s' % v,
        elif k == 19 or k == 20 or k == 21:
            v = v.replace(' ', '')
            print '%15s' % v,
        elif k == 22:  # email
            print '%25s' % v,
        elif k == 31:  # date and time
            print '%20s' % v,
        elif k == 32:
            print '%6s' % v,
        else:
            print '%3s' % v,
    time.sleep(0.1)
    print '\n'


def lastThreeMeta(lst):
    if len(lst) < 23:
        print ' Bad list : ',lst
        return []
    temp = lst[0:24]
    for k in range(33 - len(temp)):
        temp.append('')
    # 最后三个字段
    for k in range(1, 4):
        temp[-k] = lst[-k]
    # 处理Email后面的 8 个字段的值
    for k,v in enumerate(lst[23:]):
        if k >=7:
            break
        temp[23+k] = v
    lst = temp
    return lst


def saveToMySQL(lst):
    try:
        db = MySQLdb.connect(
            host='localhost', db='shifenzheng', user='root', passwd='root', charset='utf8')
        sql = 'insert into shifenzheng (Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
        cursor = db.cursor()
        #cursor.executemany(sql,lst)
        #db.commit()

        part = list()
        for k in range(len(lst)):
            part.append(lst[k])
            if k % 100 == 0:
                print 'k :', k,
                print cursor.executemany(sql, part)
                db.commit()
                part = []
        print cursor.executemany(sql, part)
        db.commit()
        print 'length of list :',len(lst)
    except Exception as ex:
        print ex
    finally:
        cursor.close()
        db.close()


readBadFile()

# try:
# db = MySQLdb.connect(host='localhost',db='shifenzheng',user='root',passwd='root')
# cursor = db.cursor()
# sql = 'select * from shifenzheng'
# sql = 'select * from co_data_raw limit 100'
# cursor.execute(sql)
# data = cursor.fetchone()
# data=cursor.fetchall()
# for d in data:
#    print d
#
#
# cursor.close()
# db.close()

# MySQL 建表脚本，以ID列对表做Range分区，每个分区大约200W条记录
# 可以按需要对某些列增加索引
"""
create table shifenzheng (
Name nvarchar(10) not null default '' ,
CardNo nvarchar(100),
Descriot nvarchar(200),
CtfTp nvarchar(100),
CtfId nvarchar(100),
Gender nvarchar(10),
Birthday nvarchar(25),
Address nvarchar(300),
Zip nvarchar(10),
Dirty nvarchar(5),
District1 nvarchar(200),
District2 nvarchar(200),
District3 nvarchar(200),
District4 nvarchar(200),
District5 nvarchar(200),
District6 nvarchar(200),
FirstNm nvarchar(50),
LastNm nvarchar(50),
Duty nvarchar(50),
Mobile nvarchar(50),
Tel nvarchar(50),
Fax nvarchar(50),
EMail nvarchar(100),
Nation nvarchar(50),
Taste nvarchar(50),
Education nvarchar(150),
Company nvarchar(250),
CTel nvarchar(50),
CAddress nvarchar(250),
CZip nvarchar(50),
Family nvarchar(50),
Version datetime,
id int not null,
primary key (id)
)ENGINE=MyISAM default charset=utf8 partition by range(id)(
  partition p0 values less than (2000000),
  partition p1 values less than (4000000),
  partition p2 values less than (6000000),
  partition p3 values less than (8000000),
  partition p4 values less than (10000000),
  partition p5 values less than (12000000),
  partition p6 values less than (14000000),
  partition p7 values less than (16000000),
  partition p8 values less than (18000000),
  partition p9 values less than (20000000),
  partition p10 values less than  MAXVALUE

);
"""
