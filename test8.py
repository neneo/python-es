#!/usr/bin/python
#-*- coding=utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")

if __name__ == '__main__':
    answer = {
        'isabled':1,
        'weight':3,
        'creator':'管理员',
        'age':7,
        'agegroup':'4 2 1',
        'editor':'管理员',
        'answer':'天音寺里面很干净',
        'guid':'174c3f64169b41d98e42bc8eedbf4b8f',
        'isdel':0,
        'createtime':12123,
        'edittime':234324 
    }

    param = {
        "script":{
            "inline":"ctx._source.allans.add(params.answer);",
            "lang":"painless",
            "params":{
                "answer":answer
            }
        }
    }

    # res = es.get(index="gi", doc_type="group", id="4fda3052ef054baea56eb6d1df5f8ad0")
    # print json.dumps(res, ensure_ascii=False)

    # res = es.update(index="gi", doc_type="group", id="4fda3052ef054baea56eb6d1df5f8ad0", body=param)
    # print json.dumps(res, ensure_ascii=False)

    # res = es.get(index="gi", doc_type="group", id="4fda3052ef054baea56eb6d1df5f8ad0")
    # print json.dumps(res, ensure_ascii=False)

    param = {
        "script":{
            "inline":"ctx._source.editor=params.editor;ctx._source.edittime=params.edittime;for(int i=0; i<ctx._source.allque.size(); i++){if(ctx._source.allque[i].guid==params.qid){ctx._source.allque[i].isdel=1;}}",
            "lang":"painless",
            "params":{
                "editor":"test001",
                "edittime":1500453137,
                "qid":"bd56667358fc4f4caeb7b92f7b48d806"
            }
        },
        "query":{
            "nested":{
                "path":"allque",
                "query":{
                    "term":{
                        "allque.guid":"bd56667358fc4f4caeb7b92f7b48d806"
                    }
                }
            }
        }
    }

    param = {"query":{"nested":{"path":"allque","query":{"term":{"allque.guid":"94001138f72d43f3883c1515f46eacc0"}}}},"script":{"inline":"ctx._source.editor=params.editor;ctx._source.edittime=params.edittime;for(int i=0; i<ctx._source.allque.size(); i++){if(ctx._source.allque[i].guid==params.qid){ctx._source.allque[i].question=params.question;ctx._source.allque[i].keywords=params.keywords;ctx._source.allque[i].editor=params.editor;ctx._source.allque[i].edittime=params.edittime;}}","lang":"painless","params":{"editor":"lu","edittime":1500530638,"keywords":"稀饭","qid":"94001138f72d43f3883c1515f46eacc0","question":"我不想吃稀饭"}}}

    # res = es.update_by_query(index="gi", doc_type="group", body=param)
    # print json.dumps(res, ensure_ascii=False)

    # res = es.get(index="gi", doc_type="group", id="4fda3052ef054baea56eb6d1df5f8ad0")
    # print json.dumps(res, ensure_ascii=False)

    param = {
        "size":0,
        "aggs":{
            "agesort":{
                "nested":{
                    "path":"allans",
                },
                "aggs":{
                    "maxage":{
                        "max":{
                            "field":"allans.age"
                        }
                    }
                }
            }
        }
    }

    param = {
        "_source":[
            "allque"
        ],
        "query":{
            "nested":{
                "path":"allque",
                "query":{
                    "term":{
                        "allque.guid":"94001138f72d43f3883c1515f46eacc0"
                    }
                }
            }
        }
    }

    res = es.search(index="gi", doc_type="group", body=param)
    print json.dumps(res, ensure_ascii=False)