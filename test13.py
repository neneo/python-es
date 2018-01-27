#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
import json
import requests
import json

from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch

def migToEs(es, idx, maptype, id, body):
    res = es.index(index=idx, doc_type=maptype, id=id, body=body)
    print(json.dumps(res, ensure_ascii=False))

def connectToDB():
    return MySQLdb.connect("172.20.0.162","putao_corpusmgmt","K3ISLNie5DNEg","putao_corpusmgmt",charset='utf8mb4')
    # return MySQLdb.connect("10.1.11.15","putao_corpusmgmt","K3ISLNie5DNEg","putao_corpusmgmt",port=3357,charset='utf8mb4')

def getGroupCount(cursor,sscn):
    strsql = "select count(id) from tab_grp where ssguid='%s';" % sscn
    cursor.execute(strsql)
    result = cursor.fetchone()
    return result[0]

def migSScn(cursor, es):
    strsql = "select * from tab_sscn;"
    cursor.execute(strsql)
    results = cursor.fetchall()

    ssl = list()
    for result in results:
        srcid = result[8]
        ssid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        srcid = result[4]
        fsid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        ss = dict()
        ss["syncid"]    = result[0]
        ss["fsid"]      = fsid
        ss["ename"]     = result[1]
        ss["editor"]    = result[2]
        ss["name"]      = result[3]
        ss["dsc"]       = result[5]
        ss["isabled"]   = result[6]
        ss["isdel"]     = result[7]
        ss["guid"]       = ssid
        ss["group-count"] = getGroupCount(cursor, result[8])
        migToEs(es, "si", 'sscn', ssid, ss) 
    

def migFScn(cursor, es):
    strsql = "select * from tab_fscn;"
    cursor.execute(strsql)
    results = cursor.fetchall()

    for result in results:
        srcid = result[7]
        fsid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        str.replace
        fs = dict()
        fs["syncid"]    = result[0]
        fs["name"]      = result[1]
        fs["ename"]     = result[2]
        fs["editor"]    = result[3]
        fs["dsc"]       = result[4]
        fs["isabled"]   = result[5]
        fs["isdel"]     = result[6]
        fs["guid"]        = fsid

        migToEs(es, "fi", 'fscn', fsid, fs) 

def getCps(cursor, cpsid):
    strsql = "select * from tab_cps where guid='%s';" % cpsid
    cursor.execute(strsql)
    result = cursor.fetchone()
    corpus = dict()
    srcid = result[3]
    cpsid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
    corpus["dsc"]       = result[2]
    corpus["corpusid"]  = cpsid
    corpus["creator"]   = result[4]
    corpus["editor"]    = result[5]
    corpus["createtime"]= result[6]
    corpus["edittime"]  = result[7]
    return corpus

def getScn(cursor, ssid):
    strsql = "select * from tab_sscn where guid='%s';" % ssid
    cursor.execute(strsql)
    result = cursor.fetchone()
    scn = dict()
    srcid = result[4]
    fsid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
    scn["scene"] = result[3]
    scn["fsid"]  = fsid
    return scn    

def getAllQue(cursor, gid):
    strsql = "select * from tab_q where groupid='%s';" % gid
    cursor.execute(strsql)
    results = cursor.fetchall()

    allque = list()
    for result in results:
        srcid = result[9]
        qid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        que = dict()
        que["syncid"]       = result[0]
        que["question"]     = result[1]
        que["keywords"]     = result[2]
        que["creator"]      = result[3]
        # que["gid"]          = result[4]
        que["createtime"]   = result[5]
        que["edittime"]     = result[6]
        que["editor"]       = result[7]
        que["isdel"]        = result[8]
        que["guid"]          = qid
        allque.append(que)

    return allque

def agegroup(age):
    ages = ""
    for i in range(5):
        a = 2**i

        b = age & a
        if b:
            ages += str(a)
            ages += " "
    
    return ages[0:-1]

def getAllAns(cursor, gid):
    strsql = "select * from tab_a where groupid='%s';" % gid
    cursor.execute(strsql)
    results = cursor.fetchall()

    allans = list()
    for result in results:
        srcid = result[10]
        aid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        ans = dict()
        age = int(result[3])
        ages = agegroup(age)
        ans["syncid"]       = result[0]
        ans["answer"]       = result[1]
        ans["weight"]       = result[2]
        ans["age"]          = result[3]
        ans["agegroup"]     = ages
        ans["creator"]      = result[5]
        ans["editor"]       = result[6]
        ans["createtime"]   = result[7]
        ans["edittime"]     = result[8]
        ans["isdel"]        = result[9]
        ans["guid"]          = aid
        ans["isabled"]      = result[11]
        allans.append(ans)

    return allans

def migGroup(cursor, es):
    strsql = "select * from tab_grp;"
    cursor.execute(strsql)
    results = cursor.fetchall()
    
    for result in results:
        srcid = result[6]
        gid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        srcid = result[4]
        sid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        grp = dict()
        grp["syncid"]   = result[0]
        grp["isabled"]  = result[2]
        grp["isdel"]    = result[3]
        # grp["ssid"]   = result[4] 
        grp["hasque"]   = result[5]
        grp["guid"]       = gid
        grp["creator"]  = result[7]
        grp["editor"]   = result[8]
        grp["createtime"]   = result[9]
        grp["edittime"]     = result[10]
        grp["corpus"]       = getCps(cursor, result[1])
        scn = getScn(cursor, result[4])
        grp["scene"] = scn["scene"]
        grp["fscene-guid"] = scn["fsid"]
        grp["scene-guid"] = sid
        grp["allque"] = getAllQue(cursor, result[6])
        grp["allans"] = getAllAns(cursor, result[6])

        migToEs(es, "group-index", 'group', gid, grp)

def migCps(cursor, es):
    strsql = "select * from tab_cps;"
    cursor.execute(strsql)
    results = cursor.fetchall()

    for result in results:
        srcid = result[3]
        cpsid = srcid[0:8] + srcid[9:13] + srcid[14:18] + srcid[19:23] + srcid[24:]
        cps = dict()
        cps["syncid"]   = result[0]
        cps["dsc"]      = result[2]
        cps["guid"]     = cpsid
        cps["creator"]  = result[4]
        cps["editor"]   = result[5]
        cps["createtime"]   = result[6]
        cps["edittime"]     = result[7]
        migToEs(es, "corpus-index",'corpus', cpsid, cps)

def mig(cursor, es):
    migFScn(cursor, es)
    migSScn(cursor, es)
    migGroup(cursor, es)
    migCps(cursor, es)

def main():
    # es = Elasticsearch("http://10.172.97.179:9200")
    es = Elasticsearch("http://172.20.6.13:9200")
    drv = connectToDB()
    cursor = drv.cursor()

    mig(cursor, es)

    cursor.close()
    drv.commit()
    drv.close()


if __name__=='__main__':
    main()
