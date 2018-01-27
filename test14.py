#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("http://172.20.4.9:9200")

if __name__ == '__main__':

    param = {
        'properties':{
            "package_name":{
                'type':'text',
                'fielddata':'true'
            },
            "package_version":{
                'type':'text',
                'fielddata':'true'
            }
        }
    }

    res = es.indices.put_mapping(index='ptlog_paios_power_value',body=param,doc_type='day-data-2017', update_all_types=True)
    print(json.dumps(res, ensure_ascii=False))

    es.indices.refresh('ptlog_paios_power_value')

    param = {
        "size":0,
        "query":{
            "bool": {
                "must": [
                        {"match": { "device_id": "none" } } ,
                        {"range": {
                                "time": {
                                    "gte": 1506787200,
                                    "lte": 1509465599
                                }
                            }}
                ]
                    }
        },
        "aggs": {
            "first": {
                "terms":{
                    "field":"package_name",
                    "field":"package_version"
                },
                "aggs":{
                    "test":{
                        "top_hits":{
                            "_source":["package_name", "package_version"],
                            "size":1
                        }
                    }
                }
            }  
        }
    }

    res = es.search(index='ptlog_paios_power_value', body=param)
    print(json.dumps(res, ensure_ascii=False))