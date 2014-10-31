# -*- coding:utf-8 -*-
#!/usr/bin/python

#from mmap import mmap, ACCESS_READ
#from xlrd import open_workbook
import xlrd
import xlwt
import xlutils.copy
import xlutils.display
import xlutils.view
from xlrd.sheet import Cell
from xlutils.display import cell_display
import xml.dom.minidom
import os


def readxml(xmlfile):
    dom = xml.dom.minidom.parse(xmlfile)
    root = dom.documentElement
    # print root.nodeName,root.nodeValue,root.nodeType
    # print root.ELEMENT_NODE
    afns = root.getElementsByTagName('AFN')
    dicAll = {}
    for afn in afns:
        dic = {}
        dic['afn_NO'] = afn.getAttribute('NO')
        dic['afn_desc'] = afn.getAttribute('desc')
        # print '\nafn=%s,%s' % (afn_NO, afn_desc)
        for fn in afn.getElementsByTagName('FN'):
            if not fn.hasAttribute('NO'):
                continue
            dic['fn_NO'] = int(fn.getAttribute('NO'))
            dic['fn_desc'] = fn.getAttribute('desc')
            dic['fn_up'] = fn.getAttribute('decode_up_stream')
            dic['fn_down'] = fn.getAttribute('decode_down_stream')
            dic['fn_di'] = fn.getAttribute('di')
            dic['fn_datatype'] = fn.getAttribute('data_type')
            # print '%s,%s,%s,%s,%s,%s' % (fn_NO, fn_desc, fn_up, fn_down,
            # fn_di, fn_datatype)
            k = str(dic['afn_NO']) + str(dic['fn_NO'])
            dicAll[k] = dic
    print ('reand xml done! ')
    # print dicAll
    return dicAll


def readxls(xlsfile):
    book = xlrd.open_workbook(xlsfile)
    sheet = book.sheet_by_name(u'Sheet1')
    print sheet.nrows

    # gw_dataitem_id,afn_code,f_code,f_name,data_len,unit,dataitem_map,
    # decode_upstream,decode_downstream,datatype,remark,isshow,isparentitem
    arr = []

    for i in range(sheet.nrows):
        if i == 0:
            continue  # without title
        # print sheet.row(i)
        arr.append(sheet.row(i))
    print ' read xls done! totalline = ', len(arr)
    return arr


def modify_xls(xml_dic, xls_arr, xlsfile1, xlsfile2):
    print 'fodify_xls functions ...'
    print 'xml_dic length = %s, xls_arr length = %s', (len(xml_dic), len(xls_arr))
    book1 = xlrd.open_workbook(xlsfile1)
    workbook = xlutils.copy.copy(book1)
    sheet = workbook.add_sheet(u'Sheet2', cell_overwrite_ok=True)

    title = [
        'gw_dataitem_id',
        'afn_code',
        'f_code',
        'f_name',
        'data_len',
        'unit',
        'dataitem_map',
        'decode_upstream',
        'decode_downstream',
        'datatype',
        'remark',
        'isshow',
        'isparentitem']
    for i in range(len(title)):
        sheet.write(0, i, title[i])

    xml_dic_existed_id = []

    for i in range(len(xls_arr)):
        # gw_dataitem_id,afn_code,f_code,f_name,data_len,unit,dataitem_map,
        # decode_upstream,decode_downstream,datatype,remark,isshow,isparentitem
        r = xls_arr[i]
        sheet.write(i, 0, r[0].value)
        sheet.write(i, 1, r[1].value)
        sheet.write(i, 2, r[2].value)
        sheet.write(i, 3, r[3].value)  # f_name
        sheet.write(i, 4, r[4].value)
        sheet.write(i, 5, r[5].value)
        sheet.write(i, 6, r[6].value)  # dataitem_map
        sheet.write(i, 7, r[7].value)  # decode_upstream
        sheet.write(i, 8, r[8].value)  # decode_downstream
        sheet.write(i, 9, r[9].value)  # datatype
        sheet.write(i, 10, r[10].value)
        sheet.write(i, 11, r[11].value)
        sheet.write(i, 12, r[12].value)
        # modify exist data-row base on xml-data, if there are existed,
        # then  xml-data -->> overwrite -->> xls-data
        key = str(r[1].value).encode('hex')+str(r[2].value)
        dic = xml_dic.get(key)
        if dic is not None:
            xml_dic_existed_id.append(key)
            sheet.write(i, 3, str(dic['fn_desc']))
            sheet.write(i, 6, str(dic['fn_di']))
            sheet.write(i, 7, dic['fn_up'])
            sheet.write(i, 8, dic['fn_down'])
            sheet.write(i, 9, dic['fn_datatype'])

    # filtter existed data-row in xml-file, and add new xml-data to xmls
    new = {}
    for (k, v) in xml_dic.items():
        if k not in xml_dic_existed_id:
            new[k] = v

    # add new row to xls
    index = len(xls_arr)
    for (k, v) in new.items():
        index = index+1
        sheet.write(i, 0, index)
        sheet.write(i, 1, v['afn_NO'])
        sheet.write(i, 2, v['fn_NO'])
        sheet.write(i, 3, v['fn_desc'])  # f_name
        sheet.write(i, 4, 0)  # data_len
        sheet.write(i, 5, '')  # unit
        sheet.write(i, 6, v['fn_di'])  # dataitem_map
        sheet.write(i, 7, v['fn_up'])  # decode_upstream
        sheet.write(i, 8, v['fn_down'])  # decode_downstream
        sheet.write(i, 9, v['fn_datatype'])  # datatype
        sheet.write(i, 10, '')  # remark
        sheet.write(i, 11, 1)  # isshow
        sheet.write(i, 12, 0)  # isparent

    # save
    workbook.save(xlsfile2)
    print ' save to xlsfile %s', xlsfile2


xmlfile = r'''C:\workspace\pro\FEP_V1\com.techenframework.protocol.gw\src\com\techenframework\protocol\gw\frame\afnfn-method.xml'''
xlsfile = u'C:\工作\kernel_gw_dataitem.xls'
xlsfile2 = u'C:\工作\kernel_gw_dataitem2.xls'


xml_dic = readxml(xmlfile)
xls_arr = readxls(xlsfile)
modify_xls(xml_dic, xls_arr, xlsfile, xlsfile2)
