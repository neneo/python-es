#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("http://10.1.11.78:9200")

if __name__ == '__main__':
    param = {
        'query':{
            'bool':{
                'must':[
                    {
                        'term':{
                            'device_id':'pico-P2BGCL300012-1'
                        }
                    },
                    {
                        'term':{
                            'request':'/api/login'
                        }
                    }
                ]
            }
        }
    }

    param = {
        'size':100,
        'query':{
            'match_all':{}
        }
    }

    res = es.search(index='gi', doc_type='group', body = param)
    print json.dumps(res, ensure_ascii=False)