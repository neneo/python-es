#!/bin/bash/python3
#-*- coding:utf-8 -*-

"""分组聚合查询测试"""

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")

if __name__ == '__main__':
    param = {
        "size":0,
        # "_source":["ss"],
        # "query":{
        #     "match":{
        #         "isdel":0
        #     },
        #     "match":{
        #         "ss.isdel":0
        #     }
        # },
        "aggs":{
            "sss":{
                "cardinality":{
                    "field":"sscn.sid"
                }
            }
        }
    }
    # res = es.search(index="scene-index", body=param)
    # print(json.dumps(res, ensure_ascii=False))

    param = {
        "size":0,
        "aggs":{
            "scenes":{
                "terms":{
                    "field":"scene-guid",
                    "size":100
                }
            }
        }
    }

    # res = es.search(index="group-index", body=param)
    # res = es.search(index="group-index", body=param)
    # print(json.dumps(res, ensure_ascii=False))

    # aggs = res["aggregations"]
    # scenes = aggs["scenes"]
    # buckets = scenes["buckets"]
    # for scn in buckets:
    #     print(">>> %s---%s" % (scn["key"], scn["doc_count"]))
    # print(json.dumps(res))


    param = {
        "size":0,
        "query":{
            "term":{
                "scene-guid":"189e46fecdf641208c5be5196b201aa7"
            }
        },
        "aggs":{
            "groupcount":{
                "cardinality":{
                    "field":"guid"
                }
            }
        }
    }

    # res = es.search(index="gi", body=param)
    # print (json.dumps(res, ensure_ascii=True))


    # param = {"allans":[],"allque":[],"corpus":{"corpusid":"3574d30acb6d450c92e82ef4b0297063","createtime":1493978371,"creator":"管理员","dsc":" 小q语料","editor":"管理员","edittime":1493978371},"createtime":1499413478,"creator":"lu","editor":"lu","edittime":1499413478,"fscene-guid":"56430faa73a144578b3dddcd09a88665","guid":"33ec43038d0442b5a08a9516ecb2ec74","hasque":1,"isabled":1,"isdel":0,"scene":"发现美洲新大陆","scene-guid":"189e46fecdf641208c5be5196b201aa7"}
    # res = es.index(index="gi", doc_type="group", id="33ec43038d0442b5a08a9516ecb2ec74", body=param)
    # print(json.dumps(res, ensure_ascii=True))

    param = {
        "size":1000,
        "query":{
            "bool":{
                "must":[
                    {
                        "term":{
                            "isdel":0
                        }
                    },
                    {
                        "term":{
                            "hasque":0
                        }
                    }
                ]
            }
        }
    }

    # res = es.search(index="gi", body=param)
    # print (json.dumps(res, ensure_ascii=False))

    # param = {"isabled": 1, "creator": "管理员", "allque": [], "fscene-guid": "9cec552e3edb488180fb47fc4960812b", "scene": "测试一下", "allans": [{"isabled": 1, "weight": 4, "creator": "管理员", "age": 3, "editor": "管理员", "answer": "哈哈，不告诉你", "isdel": 1, "guid": "4aedbbce96454b65b1108cab1ef2450b", "createtime": 1493982607, "agegroup": "1 2", "edittime": 1}, {"isabled": 1, "weight": 9, "creator": "creator01", "age": 1, "editor": "creator01", "answer": "吃过了", "isdel": 0, "guid": "bcc254ddd8b44694877de8e1f3b3926e", "createtime": 1495506783, "agegroup": "1", "edittime": 1495506783}, {"isabled": 1, "weight": 9, "creator": "creator01", "age": 1, "editor": "editor01", "answer": "吃过了", "isdel": 0, "guid": "65598fa1121849f2becdc3afc5ff3557", "createtime": 1495506824, "agegroup": "1", "edittime": 1495507267}], "createtime": 1493982607, "scene-guid": "76a2c9429fe64d6095db04ae256093be", "editor": "", "hasque": 0, "corpus": {"creator": "管理员", "dsc": " 小q语料", "editor": "管理员", "corpusid": "3574d30acb6d450c92e82ef4b0297063", "createtime": 1493978371, "edittime": 1493978371}, "guid": "1cdf46daba9b45b28e4e80d9541d09c5", "isdel": 1, "edittime": 1493983341}

    # res = es.index(index="gi", doc_type="group", id="1cdf46daba9b45b28e4e80d9541d09c5", body=param)
    # print (json.dumps(res, ensure_ascii=False))
    # res = es.get(index="gi", doc_type="group", id="1398b1da40c14f95aadd37f3435c3814")
    # print (json.dumps(res, ensure_ascii=False))

    # param = {
    #     "doc":{
    #         "isdel":0
    #     }
    # }

    # res = es.update(index="gi", doc_type="group", id="1cdf46daba9b45b28e4e80d9541d09c5", body=param)
    # print res

    # res = es.get(index="gi", doc_type="group", id="1cdf46daba9b45b28e4e80d9541d09c5")
    # print (json.dumps(res, ensure_ascii=False))

    param = {
        # "doc":{
        #     "scene-guid":"76a2c9429fe64d6095db04ae256093beaaaa"
        # },
        "script":{
            "inline":"ctx._source.corpus.corpusid=params.corpusid;",
            "lang":"painless",
            "params":{
                "corpusid":"3574d30acb6d450c92e82ef4b0297063"
            }
        }
    }

    # res = es.update(index="gi", doc_type="group", id="1cdf46daba9b45b28e4e80d9541d09c5", body=param)
    # print (json.dumps(res, ensure_ascii=False))
    # res = es.get(index="gi", doc_type="group", id="1cdf46daba9b45b28e4e80d9541d09c5")
    # print (json.dumps(res, ensure_ascii=False))

    param = {
        "size":0,
        "query":{
            "bool":{
                "must":[
                    {
                        "term":{
                            "isdel":0
                        }
                    },
                    {
                        "nested":{
                            "path":"allans",
                            "query":{
                                "term":{
                                    "allans.isdel":0
                                }
                            }
                        }
                    }
                ]
            }
        },
        "aggs":{
            "allans":{
                "nested":{
                    "path":"allans"
                },
                "aggs":{
                    "allauthors":{
                        "terms":{
                            "field":"allans.creator",
                            "size":10000
                        }
                    }
                }
            }
        }
    }

    res = es.search(index="gi", doc_type="group", body=param)
    print json.dumps(res, ensure_ascii=False)
