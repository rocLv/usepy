# -*- coding:utf-8 -*-

import os
import _winreg
#import shutil
print("Clean history ...")

#Jumplist template folder "%APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations"
print "-> Clean jumplistpath ..."
recentpath1 = os.environ.get("APPDATA") +"\Microsoft\Windows\Recent\AutomaticDestinations"
recentpath2 = os.environ.get("APPDATA") +"\Microsoft\Windows\Recent\CustomDestinations"
try:
    if os.path.isdir(recentpath1):
        for f in os.listdir(recentpath1):
            os.remove(recentpath1 + "\\" + f)
            print "remove."+f

    if os.path.isdir(recentpath2):
        for f in os.listdir(recentpath2):
            os.remove(recentpath2 + "\\" + f)
            print "remove."+f

except Exception,ex:
    #print Exception,":",ex
    pass

print "<- Finished. "

print "Clear WIN+Run history ..."

# 删除运行历史记录
# 更多操作注册表详情 http://www.cnblogs.com/JeffreySun/archive/2010/01/04/1639117.html
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU",0,_winreg.KEY_ALL_ACCESS)
#print key
namelist=[]
try:
    i =0
    while True:
        name,value,typ= _winreg.EnumValue(key,i)
        #print "i:%s, n:%s, v:%s, t:%s" %(i,name,value,ty)  
        _winreg.DeleteValue(key,name)
        i +=1
except WindowsError,e:
   #print Exception,e,"_winreg.DeleteValue error"
   pass
finally:
    _winreg.CloseKey(key)

print "<- Finished"




