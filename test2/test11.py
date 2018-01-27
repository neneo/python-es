#!/usr/bin/python
#-*- coding:utf-8 -*-

import redis
import xdrlib 
import sys
import xlrd
import re

# if __name__ == '__main__':
#     r = redis.Redis(host="10.1.11.34", port=6379, db=0)

#     r.set('test', '您好:3')
#     print r.get('test')

def open_excel(file= 'file1.xls'):

    try:

        data = xlrd.open_workbook(file)

        return data

    except Exception,e:

        print str(e)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引

def excel_table_byindex(file= 'file1.xls',colnameindex=0,by_index=0, isQ = True):

    data = open_excel(file)

    table = data.sheets()[by_index]

    nrows = table.nrows #行数

    ncols = table.ncols #列数

    colnames =  table.row_values(colnameindex) #某一行数据 

    # for colname in colnames:

    #     print colname

    list =[]

    dstcols = []

    if(isQ):

        dstcols = [3,4,5] #只要第3、4、5两列

    else:

        dstcols = [3,6,7]

    for rownum in range(1,nrows):

         row = table.row_values(rownum)

         if row:

             app = {}

             for i in dstcols:

                app[colnames[i]] = row[i] 

             list.append(app)

    return list



#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称

def excel_table_byname(file= 'file1.xls',colnameindex=0,by_name=u'Sheet1'):

    data = open_excel(file)

    table = data.sheet_by_name(by_name)

    nrows = table.nrows #行数 
    print ">>> file1.xls has " + str(nrows) + " rows"

    colnames =  table.row_values(colnameindex) #某一行数据 

    list =[]

    for rownum in range(1,nrows):

         row = table.row_values(rownum)

         if row:

             app = {}

             for i in range(len(colnames)):

                app[colnames[i]] = row[i]

             list.append(app)

    return list



def writeToJsonQ(strRows, fd):

    strA = ""

    strQ = ""

    rows = strRows[u"例句"]

    rows = rows.split("|")

    row = rows[0].strip("\n").strip("？").strip("?")

    if len(row) > 1:
        row = row.split("/")
        row = row[0].strip("\n").strip("？").strip("?")
        strQ = row

    rows = strRows[u'回答/定义']
    rows = rows.split("\n")
    for row in rows:
        if len(row) == 0:
            continue

        row = row.strip("\n").strip("？").strip("?").strip("；")

        fd.write(b"\t\t\"")

        fd.write(row)

        fd.write(b"\":")

        fd.write(b"\"")

        fd.write(strQ)

        fd.write("\",\n")



    pattern = re.compile(r"\d" + u'、')

    rows = strRows[u'回复扩展']

    rows = rows.split("\n")

    for row in rows:

        row = row.strip().strip("|").rstrip(u'。').rstrip(u'？').rstrip(u'！')

        mstr = pattern.match(row)

        if(mstr):

            row = row.lstrip(mstr.group())

        if(len(row) != 0):

            fd.write(b"\t\t\"")

            fd.write(row)

            fd.write(b"\":")

            fd.write(b"\"")

            fd.write(strQ)

            fd.write("\",\n")



def writeToJsonA(strRows, fd):

    strA = "["

    strQ = "\t\t\""

    rows = strRows[u"例句"]

    rows = rows.split("|")

    row = rows[0].strip("\n").strip("？").strip("?")

    if len(row) > 1:

        row = row.split("/")

        row = row[0].strip("\n").strip("？").strip("?")

        strQ += row

        strQ += "\":"



    rows = strRows[u"回答"]

    rows = rows.split("\n")

    for row in rows:

        row = row.strip("|")

        if len(row) == 0:

            continue

        strA += "\""

        strA += row

        strA += "\","



    rows = strRows[u'回答选择']

    rows = rows.split("|")

    for row in rows:

        row = row.strip()

        strA += "\""

        strA += row

        strA += "\","

    strA = strA[0:-1]

    strA += "],"

    fd.write(strQ)

    fd.write(strA)

    fd.write("\n")



def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    tables = excel_table_byindex()
    with open("./qas", "wb") as fd:
        for rows in tables:
            writeToJsonQ(rows, fd)

    #tables = excel_table_byindex(isQ = False)

    #with open("./ans", "wb") as fd:

    #    fd.write(b"{\n")

    #    fd.write(b"\t10003:{\n")

    #    for rows in tables:

    #        writeToJsonA(rows, fd)

    #    fd.write(b"\t}\n")

    #    fd.write(b"}")



#    tables = excel_table_byname()

#    for row in tables:

#        print row



if __name__=="__main__":
    main()