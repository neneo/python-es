#!/bin/bash/python3
#-*- coding:utf-8 -*-

import time
import json
import requests


import time
import json
import requests

import sys
 

from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://10.1.11.78:9200")

if __name__ == '__main__':
    # param = {
    #     "query":{
    #         "match_all":{}
    #     }
    # }

    param = {"_source":["guid"],"query":{"term":{"ename":"diet"}}}

    param = {"query":{"match":{"dsc":"通用语料"}}}

    param = {
        # 'size':5,
        'query':{
            'match_all':{}
        }
    }

    param = {
        'from':0,
        "size":20,
        "sort":{
            'edittime':{
                'order':'desc'
            }
        },
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
                                "bool":{
                                    "must":[
                                        {
                                            "term":{
                                                "allans.isdel":0
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ],
                "should":[
                    {
                        "bool":{
                            "must":[
                                {
                                    "term":{
                                        "hasque":1
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allque",
                                        "query":{
                                            "term":{
                                                "allque.isdel":0
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "bool":{
                            "must":[
                                {
                                    "term":{
                                        "hasque":0
                                    }
                                }
                            ]
                        }
                    } 
                ],
                "minimum_should_match":1
            }
        }
    }

    # res = es.get(index='gi', doc_type='group', id='c98520bf2f42456985f6be1718d14cd5')
    # print json.dumps(res, ensure_ascii=False)

    # res = es.search(index="gi", body=param)
    # print json.dumps(res, ensure_ascii=False)    

    param = {
        # 'size':5,
        'query':{
            'match_all':{}
        }
    }
    res = es.delete_by_query(index='fi', doc_type='fscn', body=param)
    res = es.delete_by_query(index='si', doc_type='sscn', body=param)
    res = es.delete_by_query(index='gi', doc_type='group', body=param)
    res = es.delete_by_query(index='ri', doc_type='record', body=param)
    res = es.delete_by_query(index='gr', doc_type='grouprd', body=param)
    # print res

    # param = {"aggs":{"maxgid":{"max":{"field":"syncid"}}},"size":0}

    # param = {
    #     'query':{
    #         "term":{
    #             "syncid":80
    #         }
    #     }
    # }

    # res = es.search(index="gi", body=param)
    # print json.dumps(res, ensure_ascii=False)

    # res = es.indices.get_mapping(doc_type='corpus',index='ci')
    # print res

    # param = {"_source":["date","editor","corpus","operatetype","count"],"from":0,"query":{"bool":{"must":[{"match_all":{}}]}},"size":15,"sort":[{"date":{"order":"desc"}},{"editor":{"order":"asc"}},{"corpus":{"order":"asc"}},{"operatetype":{"order":"asc"}}]}

    # param = {"query":{"bool":{"must":[{"term":{"date":1504800000}},{"term":{"editor":"admin"}},{"match":{"corpus":"通用语料库"}},{"term":{"operatetype":"add"}}]}}}

    # res = es.search(index="ri", body=param)
    # print json.dumps(res, ensure_ascii=False)

    # param = {
    #     "properties":{
    #         "corpusid":{
    #             'fielddata':'true',
    #             "type": "text"
    #         }
    #     }
    # }

    # param = {"corpus":"通用语料库","corpusid":"7fb24dfa39b441a3be683ad15d5db75d","counter":0,"date":1504800000,"editor":"admin","ids":[],"operatetype":"add"}

    # res = es.index(index="ri", doc_type='record', id='1', body=param, version=1504800000, version_type='external')
    # print json.dumps(res, ensure_ascii=False)

    # es.indices.refresh('ri')

    # res = es.get(index = 'ri', doc_type='record', id = '1')
    # print json.dumps(res, ensure_ascii=False)

    # res = es.indices.put_mapping(index='ri', doc_type='record', body=param)
    # print res

    # res = es.indices.get_mapping(index='ri', doc_type='record')
    # print res

    param = {
        'query':{
            'match_all':{}
        }
    }

    # res = es.search(index="ri", body=param)
    # print json.dumps(res, ensure_ascii=False) 

    # res = es.search(index="ci", body=param)
    # print json.dumps(res, ensure_ascii=False) 

    # es.delete(index="ci", doc_type="corpus", id='cbcb2e68b1cd4ccca6840659f81ae2d5')
    # print json.dumps(res, ensure_ascii=False) 

    # es.indices.refresh('gi')

    # res = es.search(index="gi", body=param)
    # print json.dumps(res, ensure_ascii=False)    

    # param = {
    #     "_source":[
    #         "guid"
    #     ],
    #     "query":{
    #         "term":{
    #             "ename":"s_life_sleep"
    #         }
    #     }
    # }
    # param = {"_source":["guid"],"query":{"term":{"ename":"s_life_sleep"}}}
    # param = {"_source":["guid"],"query":{"term":{"ename":"s_life_sleep"}}}
    # res = es.search(index="si", body=param)
    # print json.dumps(res, ensure_ascii=False)    


    param = {
        "_source":[
            "guid"
        ],
        "query":{
            "term":{
                "dsc":"最新"
            }
        }
    }


    # res = es.search(index="ci", body=param)
    # print json.dumps(res, ensure_ascii=False)    

    # res = es.delete(index="ri", doc_type="record", id='AV6T9nrYR92W50PHkItp')

    # es = Elasticsearch("http://10.1.11.42:9200")
    # param = {
    #     'properties':{
    #         'device_id':{
    #             'type':'text',
    #             'fielddata':'true'
    #         },
    #         'package_name':{
    #             'type':'text',
    #             'fielddata':'true'
    #         },
    #         'package_version':{
    #             'type':'text',
    #             'fielddata':'true'
    #         }
    #     }
    # }

    # res = es.indices.put_mapping(doc_type='day-data-2017', body=param, index='ptlog_paios_power_value')
    # print(json.dumps(res, ensure_ascii=False))

    # param = {
    #     "size":0,
    #     "query":{
    #         # "match_all":{}
    #         "range":{
    #             "time": {
    #                 "gte": 1505404800,
    #                 "lte": 1505577600
    #             }
    #         }
    #     },
    #     "aggs": {
    #         "first": {
    #             'terms':{
    #                 'field':"device_id"
    #             }
    #         }  
    #     }
    # }

    # param = {
    #     "size":0,
    #     "query":{
    #         "range":{
    #             "time": {
    #                 "gte": 1505404800,
    #                 "lte": 1505577600
    #             }
    #         }
    #     },
    #     "aggs": {
    #         "first": {
    #             'terms':{
    #                 'field':'package_name',
    #                 'field':'package_version'
    #             },
    #             'aggs':{
    #                 'test':{
    #                     'top_hits':{
    #                         '_source':['package_name', 'package_version'],
    #                         'size':1
    #                     }
    #                 }
    #             }
    #         }  
    #     }
    # }

    # res = es.search(index="ptlog_paios_power_value", body=param)
    # print json.dumps(res, ensure_ascii=False)