#!/bin/bash/python3
#-*- coding:utf-8 -*-

"""物理删除测试"""

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")

if __name__=='__main__':
    param = {
        "_source":[
            "ename",
            "nam",
            "guid",
            "sscn.ename",
            "sscn.guid",
            "sscn.name",
            "sscn.group-count",
            "sscn.isabled"
        ],
        "query":{
            "bool":{
                "must":[
                    {
                        "match":{
                            "isdel":0
                        }
                    },
                    {
                        "match":{
                            "guid":"ec4bd62374004d1d9eab9ea190071089"
                        }
                    },
                    {
                        "nested":{
                            "path":"sscn",
                            "query":{
                                "match":{
                                    "sscn.isdel":0
                                }
                            }
                        }
                    }
                ]
            }
        }
    }

    # param = {
    #     "_source":["ename"],
    #     "query":{
    #         "match":{
    #             "ename":"nimeide"
    #         } 
    #     }
    # }

    param = {
        "_source":[
            "guid",
            # "sscn.name",
            # "sscn.ename",
            "sscn.guid",
            # "sscn.editor",
            # "sscn.dsc",
            # "sscn.isabled",
            # "sscn.isdel",
            "sscn.group-count"
        ],
        "query":{
            "bool":{
                "must":[
                    {
                        "match":{
                            "isdel":0
                        }
                    },
                    {
                        "nested":{
                            "path":"sscn",
                            "score_mode":"max",
                            "query":{
                                "bool":{
                                    "must":[
                                        {
                                            "match":{
                                                "sscn.guid":"8b5ed838ff7c4afd84b36931834170a1"
                                            }
                                        },
                                        {
                                            "match":{
                                                "sscn.isdel":1
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            }
        }
    }

    # param = {
    #     "size":0,
    #     "query":{
    #         "bool":{
    #             "must":[
    #                 {
    #                     "match":{
    #                         "isdel":0
    #                     }
    #                 },
    #                 {
    #                     "match":{
    #                         "guid":"ab0817728e224a1ab87a49e50cba9fb2"
    #                     }
    #                 },
    #                 {
    #                     "nested":{
    #                         "path":"sscn",
    #                         "query":{
    #                             "match":{
    #                                 "sscn.isdel":0
    #                             },
    #                             "match":{
    #                                 "sscn.ename":"ssssssssssssssssssssssss"
    #                             }
    #                         }
    #                     }
    #                 }
    #             ]
    #         }
    #     },
    #     "aggs":{
    #         "sscn":{
    #             "nested":{
    #                 "path":"sscn"
    #             },
    #             "aggs":{
    #                 "sscount":{
    #                     "cardinality":{
    #                         "field":"sscn.guid"
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }

    # res = es.indices.refresh(index="scene-index")

    # res = es.delete_by_query(index='scene-index', body=param)
    # print(res)

    # res = es.delete_by_query(index='group-index', body=param)
    # print(res)

    # res = es.delete_by_query(index='corpus-index', body=param)
    # print(res)

    param = {
        "size":10000,
        "_source":[
            "guid",
            "name",
            "isabled"
        ],
        "query":{
            "bool":{
                "must":[
                    {
                        "term":{
                            "fsid":"ab0817728e224a1ab87a49e50cba9fb2"
                        }
                    },
                    {
                        "term":{
                            "isdel":0
                        }
                    }
                ]
            }
        }
    }

        # res = es.search(index='si', doc_type="sscn", body=param)
        # print(json.dumps(res, ensure_ascii=False))

    param = {
        "size":10000,
        "_source":[
            "guid",
            "allans.answer",
            "allans.isabled"
        ],
        "query":{
            "bool":{
                "must":[
                    {
                        "term":{
                            "fsid":"ab0817728e224a1ab87a49e50cba9fb2"
                        }
                    },
                    {
                        "term":{
                            "isdel":0
                        }
                    }
                ]
            }
        }
    }


    param = {
        "size":10000,
        "_source":[
            "guid",
            "isabled",
            "scene-guid"
        ],
        "query":{
            "bool":{
                "must":[
                    {
                        "term":{
                            "scene-guid":"189e46fecdf641208c5be5196b201aa7"
                        }
                    },
                    {
                        "term":{
                            "isdel":0
                        }
                    }
                ]
            }
        }
    }

    # res = es.search(index='gi', doc_type="group", body=param)
    # print(json.dumps(res, ensure_ascii=False))

    param = {
        "query":{
            "term":{
                "ename":"sword"
            }
        }
    }


    # res = es.search(index="si", doc_type="sscn", body=param)
    # print(json.dumps(res, ensure_ascii=False))

    res = es.delete(index="si", doc_type="sscn", id="0143f5c3c60f46e9b855a20870930b8e")
    print res


    # res = es.get(index="si",doc_type="sscn", id="189e46fecdf641208c5be5196b201aa7")
    # print(json.dumps(res, ensure_ascii=False))

    # es.indices.refresh(index="si")