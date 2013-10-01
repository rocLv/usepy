# -*- coding:utf-8 -*-
#!/usr/bin/python2.7
#
# Copyright [2013] scymen@gmail.com
# Licensed under the Apache Licensed. Version 2.0 (the "licensed"):
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


""" Calculate the measurement unit of storage capacity. """

import re

mu =['B','KB','MB','GB','TB','PB','EB','ZB','YB','BB','NB','DB']
muname = ['Byte','KiloByte','MegaByte','GigaByte','TeraByte','PetaByte','ExaByte','ZettaByte','YttaByte','BrontoByte','NonaByte','DoggaByte']
muchinese=[u'字节',u'千字节',u'兆字节',u'吉字节',u'太字节',u'拍字节',u'艾字节',u'泽字节',u'尧字节',u'BrontoByte',u'NonaByte',u'DoggaByte']
reExpress =r'^[+-]?\d+[.]?\d+$'                     # Nature format
reExpress2 = r'^[+-]?\d+[.]?\d+[Ee]?[+-]?\d+$'       # Scientific notation

def getUnit(size):
    """ Calculate the measurement unit of storage capacity """
    match = re.match(reExpress,str(size)) or re.match(reExpress2,str(size))
    if match:
        index=0
        size = float(size)
        while(size > 1024.0):
            size = size / 1024.0
            index += 1
        if index >= len(mu):
            raise OverflowError,'Input size too large.'
        return '{0}{1}'.format(size,mu[int(index)])
    else:
        raise TypeError,'The type/format of Argument incorrect.'


def getFullName(name):
    """ Get fullname of unit. e.g. KB,MB,GB... """
    index = mu.index(name.upper())
    if index >=0 :
        return muname[index]
    return None


def getChineseName(name):
    """ Get Chinese name of unit. e.g. KB,MB,GB... """
    if len(name) < 3:
        index = mu.index(name.upper())
        if index >=0 :
            return muchinese[index]
    else:
        for i,item in enumerate(muname):
            if item.upper() == name.upper():
                return muchinese[i]
    return None


#print getUnit(1024*45.4567)
#print getUnit(1024*1024*45.4567)
#print getUnit(1024*1024*1024*45.45670098)
#result = 1024*1024*1024*1024*45.793234244
#result = result * result
#print result
#print getUnit(result)
#print getUnit('12312313')
#print getUnit('2398923942747872323')
#print 'kilobyte'.title()
#print getChineseName('KiloByte')
#print getFullName('MB')
#print getChineseName('eb')

