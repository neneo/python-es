#!/bin/bash/python3
#-*- coding:utf-8 -*-

"""物理删除测试"""

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")

if __name__ == '__main__':
    param = {
        "size":0,
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
                            "guid":"48a2af5cc65343168d9e123362f026db"
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
        },
        "aggs":{
            "sscn":{
                "nested":{
                    "path":"sscn"
                },
                "aggs":{
                    "sscount":{
                        "cardinality":{
                            "field":"sscn.sid"
                        }
                    }
                }
            }
        }
    }

    param = {
        "_source":[
            "ename",
            "name",
            "guid",
            "dsc",
            "editor",
            "isabled"
        ],
        "query":{
            "match":{
                "isdel":0
            }
        }
    }

    param = {
        "_source":["sscn"],
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
                            "guid":"48a2af5cc65343168d9e123362f026db"
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

    param = {
        'script':{
            "inline":"""for(int i=0;i<ctx._source.sscn.size();i++){
                if(ctx._source.sscn[i].guid=='5cc8757c125943408f6b9a5f2115c57c')
                    ctx._source.sscn[i].name=params.scnid;
            }""",
            "lang":"painless",
            'params':{
                "scnid":"我叫xxxxx"
            }
        }
    }

    param = {
        "script":{
            "inline":"""for(int i=0;i<ctx._source.sscn.size();i++)
            {
                ctx._source.sscn[i].isabled=1;
                ctx._source.sscn[i].editor=params.editor;
            }""",
            "lang":"painless",
            "params":{
                "editor":"test"
            }
        }
    }

    param = {
        "script":{
            "inline":"""for(int i=0;i<ctx._source.sscn.size();i++){
                if(ctx._source.sscn[i].guid == params.scene) {
                    ctx._source.sscn[i].name=params.name;
                    ctx._source.sscn[i].editor=params.editor;
                    ctx._source.sscn[i].dsc=params.dsc;
                }
            }""",
            "lang":"painless",
            "params":{
                "dsc":"测试",
                "editor":"lu",
                "name":"就是想测试下",
                "scene":"8b5ed838ff7c4afd84b36931834170a1"
            }
        }
    }

    # param = {
    #     "script" : {
    #         "inline":"ctx._source.ename='nimeide'",
    #         "lang":"painless"
    #     }
    # }

    # res = es.search(index='scene-index', body=param)
    # print(json.dumps(res))

    # param = {
    #     "doc":{
    #         "name":"第一次修改",
    #         "dsc":"请多指教",
    #         "editor":"lu"
    #     } 
    # }

    param = {
        "script":{
            "inline":"""for(int i=0;i<ctx._source.sscn.size();i++){
                if(ctx._source.sscn[i].guid == params.scene) {
                    ctx._source.sscn[i].editor=params.editor;
                    ctx._source.sscn[i].isabled=params.isabled;
                }
            }""",
            "lang":"painless",
            "params":{
                "isabled":0,
                "editor":"lu",
                "scene":"29994a113c044edc920ba9d21fc2f786"
            }
        }
    }

    param = {
        "script":{
            "inline":"ctx._source.sscn.add(params.ss)",
            "lang":"painless",
            "params":{
                "ss":{
                    "ename": "TESTFORADD",
                    "group-count": 20,
                    "guid": "b6b21619b7d04fe48b46beb5751d4f8a",
                    "name": "测试下增加二级场景",
                    "isabled":1,
                    "isdel":0,
                    "dsc":"二级场景添加测试",
                    "editor":"lu"
                }
            }
        }
    }

    param = {
        "script":{
            "inline":"""for(int i=0;i<ctx._source.sscn.size();i++){
                if(ctx._source.sscn[i].guid == params.scene) {
                    ctx._source.sscn[i].group-count += 1;
                }
            }""",
            "lang":"painless",
            "params":{
                "scene":"8b5ed838ff7c4afd84b36931834170a1"
            }
        }
    }

    
    # res = es.update(index='si', doc_type="fs", id='ab0817728e224a1ab87a49e50cba9fb2', body=param)
    # print(res)
    # es.indices.refresh(index="si")

    param = {"script":{"inline":"ctx._source.isabled=1;ctx._source.editor=params.editor;ctx._source.edittime=params.edittime;for(int i=0;i<ctx._source.allans.size();i++){ctx._source.allans[i].editor=params.editor;ctx._source.allans[i].edittime=params.edittime;ctx._source.allans[i].isabled=1;}","lang":"painless","params":{"editor":"lu","edittime":1499393314}}, "query":{"term":{"fsid":"ab0817728e224a1ab87a49e50cba9fb2"}}}
    # param = {"script":{"inline":"ctx._source.isabled=0;ctx._source.editor=params.editor;ctx._source.edittime=params.edittime;for(int i=0;i<ctx._source.allans.size();i++){ctx._source.allans[i].editor=params.editor;ctx._source.allans[i].edittime=params.edittime;ctx._source.allans[i].isabled=0;}","lang":"painless","params":{"editor":"lu","edittime":1499395364}}, "query":{"term":{"fsid":"ab0817728e224a1ab87a49e50cba9fb2"}}}
    
    param = {
        "doc":{
            "isdel":0
        }
    }

    res = es.update(index='si', doc_type="sscn", id='189e46fecdf641208c5be5196b201aa7', body=param)

    param = {
        "query":{
            "term":{
                "scene-guid":"189e46fecdf641208c5be5196b201aa7"
            }
        },
        "script":{
            "inline":"ctx._source.isdel=0;",
            "lang":"painless"
        }
    }
    res = es.update_by_query(index='gi', doc_type="group", body=param)
    print(res)

    # ctx._source.allans[i].editor=params.editor;ctx._source.allans[i].edittime=params.edittime;
    # for(int i=0;i<ctx._source.allans.size();i++){}
    # res = es.get(index="si", doc_type='fs', id='48a2af5cc65343168d9e123362f026db')
    # print(json.dumps(res['_source'], ensure_ascii=False))