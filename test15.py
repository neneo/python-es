#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch

# es = Elasticsearch("http://172.20.4.9:9200/ptlog_paios_power_value/day-data-2017/_search ")
es = Elasticsearch("http://172.20.4.9:9200")

if __name__ == '__main__':

    # param = {
    #     "size":20,
    #     "query":{
    #         "range":{
    #             "time": {
    #                 "gte": 1509465600,
    #                 "lte": 1512057599
    #             }
    #         }
    #     },
    #     "aggs": {
    #         "first": {
    #             "terms":{
    #                 "field":"package_name"
    #             },
    #             "aggs":{
    #                 "test":{
    #                     "top_hits":{
    #                         "_source":["package_name"],
    #                         "size":1
    #                     }
    #                 }
    #             }
    #         },
    #         "second":{
    #             "terms":{
    #                 "field":"package_version"
    #             },
    #             "aggs":{
    #                 "test":{
    #                     "top_hits":{
    #                         "_source":["package_version"],
    #                         "size":1
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }

    param = {
        "query":{
            "range":{
                "time": {
                    "gte": 1509465600,
                    "lte": 1512057599
                }
            }
        },
        "aggs": {
            "first": {
                "terms":{
                    "field":"package_name"
                },
                "aggs":{
                    "test":{
                        "top_hits":{
                            "_source":["package_name"],
                            "size":1
                        }
                    }
                },
                "aggs":{
                    "second":{
                        "terms":{
                            "field":"package_version"
                        },
                        "aggs":{
                            "test":{
                                "top_hits":{
                                    "_source":["package_version"],
                                    "size":1
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    res = es.search(index='ptlog_paios_power_value', body=param)
    print(json.dumps(res, ensure_ascii=False))