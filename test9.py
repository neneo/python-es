#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")

ma = {
    'mappings': {
        'testmap': {
            'properties': {
                'ename': {
                    'type': 'text'
                },
                'name': {
                    'type': 'text'
                },
                'docs': {
                    'type':'nested',
                    'properties':{
                        'title':{
                            'type': 'text'
                        },
                        'content':{
                            'type':'text'
                        }
                    }
                }
            }
        }
    }
}

# res = es.indices.create(index='test-index',body=ma)
# print(res)

param = {
    'ename':'test001',
    'name':'我是一个好人',
    'docs':[]
}

# res = es.index(index='test-index', doc_type='testmap', id='10001', body=param)
# print(json.dumps(res, ensure_ascii=False))

# res = es.get(index='test-index', doc_type='testmap', id='10001')
# print(json.dumps(res, ensure_ascii=False))

param = {
    "script":{
        "inline":"ctx._source.docs.add(params.doc);",
        "lang":"painless",
        "params":{
            "doc":{
                "title":"小明天天上班，坚持早到。",
                "content":"这周天气真的好热啊，到公司一身汗."
            }
        }
    }
}

# param = {
#     'doc':{
#         'docs':[]
#     }
# }

# res = es.update (index="test-index", doc_type="testmap", id="10001", body=param)
# print(json.dumps(res, ensure_ascii=False))


# res = es.get(index='test-index', doc_type='testmap', id='10001')
# print(json.dumps(res, ensure_ascii=False))

# res =  es.get(index="fi", doc_type="fscn", id="7e1cc12d17e5462ca3dbe19949585e7e")
# print(json.dumps(res, ensure_ascii=False))

param = {
    "size":0,
    "aggs":{
        "maxid":{
            "max":{
                "field":"syncid"
            }
        }
    }
}
res =  es.search(index="si", doc_type="sscn", body=param)
print(json.dumps(res, ensure_ascii=False))