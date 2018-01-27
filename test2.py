#!/usr/bin/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
# es = Elasticsearch("http://10.1.26.9:9200")
es = Elasticsearch("http://172.20.6.13:9200")
# res = es.indices.delete(index='scene-index')
# print(res)


# res = es.indices.delete(index='test-index')
# es.indices.refresh('test-index')
# print(res)


ma = {
    "settings" : {
        "number_of_shards" : 1
    },
    'mappings':{
        'test':{
            "properties": {
                "title":{
                    "type":"text",
                    # "index":"not_analyzed"
                },
                "content": {
                    "type": "text",
                    "store": "no",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "include_in_all": "true",
                    "boost": 8
                }
            }
        }
    }
}


# res = es.indices.create(index='test-index',body=ma)
# print json.dumps(res, ensure_ascii=False)

# es.indices.refresh('test-index')


doc1 = {"content":"美国留给伊拉克的是个烂摊子吗", "title":"S_LIFE_SLEEP"}
doc2 = {"content":"公安部：各地校车将享最高路权", "title":"S_LIFE_EAT"}

res = es.index(index="test-index",doc_type='zhsearch',id=1, body=doc1)
es.indices.refresh('test-index')

res = es.index(index="test-index", doc_type='zhsearch',id=2, body=doc2)
es.indices.refresh('test-index')

es.indices.refresh('test-index')

param = {
    "query" : { 
        "term" : {
            "content":"美国"
        }
    }
}

res = es.search(index="test-index", body=param)
print json.dumps(res, ensure_ascii=False)