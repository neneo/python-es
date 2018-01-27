#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("http://10.172.98.150:9200")


#----------------获取索引中相应字段内容，其他忽略-------------
# res = es.get(index="fs-index", doc_type='corpusmanage', id='7e1cc12d-17e5-462c-a3db-e19949585e7e', _source=['name','ename'])
# print(res['_source'])

#-----------------全文搜索-------------------
param = {
	'_source':['ss'],
	'query':{
		'multi_match':{
			'query':u'动物',
			'fields':['ss.name'],
			'analyzer':'chinese'
		}
	}
}

param = {"query": {"match_all": {}}}

param = {
	"query":{
		"match":{
			"guid":"51bd2af4885a4fbe9b7bb495f73feeb9"
		}
	}
}

# res = es.get(index = "fi",doc_type="fscn",id="51bd2af4885a4fbe9b7bb495f73feeb9")
# print res
# print(json.dumps(res, ensure_ascii=True))

param= {
    "size":0,
    "aggs":{
        "count":{
            "cardinality":{
                "field":"guid"
            }
        }
    }
}

# res = es.search(index="fi", body=param)
# print res

# for hit in res['hits']['hits']:
# 	data = hit["_source"]
# 	ssl = data["ss"]
# 	for ss in ssl:
# 		print(ss["name"])

# print("---------------------")

param = {
	'query':{
		'bool':{
			'must':[
				{
					'term':{
						'isdel':0
					}
				}
			]
		}
	}
}

param = {
	'query':{
		'match_all':{}
	}
}

param = {
	'_source':[
		'guid'
	],
	'query':{
		"nested":{
            "path":"allque",
            "query":{
                "term":{
                    "allque.guid":"30ca83bfd8b043388d319b6fb8c4eae0"
                }
            }
        }
	}
}

res = es.search(index = "gi", body=param)
print json.dumps(res, ensure_ascii=False)