#!/bin/bash/python3
#-*- coding:utf-8 -*-

import json
from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
# es = Elasticsearch("http://10.1.11.78:9200")
# es = Elasticsearch("http://10.172.98.150:9200")

es = Elasticsearch("http://172.20.6.13:9200")


# ----------------获取映射--------------------
# res = es.indices.get_mapping(index='corpus-index', doc_type="corpus")
# print(res)

ma = {
    'mappings': {
        'fscn': {
            'properties': {
                'ename': {
                    'type': 'text'
                },
                'isabled': {
                    'type': 'long'
                },
                'name': {
                    'type': 'text'
                },
                'dsc': {
                    'type': 'text'
                },
                'editor': {
                    'type': 'text'
                },
                'isdel': {
                    'type': 'long'
                },
                'guid': {
                    'type': 'text',
                    'fielddata':'true'
                },
                'syncid': {
                    'type': 'long'
                }
            }
        }
    }
}


mb = {
    'mappings': {
        'group': {
            'properties': {
                'isabled': {
                    'type': 'long'
                },
                'scene': {
                    'type': 'text'
                },
                'creator': {
                    'type': 'text'
                },
                'syncid': {
                    'type': 'long'
                },
                'allque': {
                    'type':'nested',
                    'properties': {
                        'creator': {
                            'type': 'text'
                        },
                        'guid': {
                            'type': 'text'
                        },
                        'syncid': {
                            'type': 'long'
                        },
                        'question': {
                            "type": "text",
                            "store": "no",
                            "term_vector": "with_positions_offsets",
                            "analyzer":"ik_max_word",
                            "search_analyzer":"ik_max_word",
                            "boost": 8
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'keywords': {
                            "type": "text",
                            "store": "no",
                            "term_vector": "with_positions_offsets",
                            "analyzer":"ik_max_word",
                            "search_analyzer":"ik_max_word",
                            "boost": 8
                        },
                        'isdel': {
                            'type': 'long'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'fscene-guid': {
                    'type': 'text'
                },
                'allans': {
                    'type':'nested',
                    'properties': {
                        'isabled': {
                            'type': 'long'
                        },
                        'weight': {
                            'type': 'long'
                        },
                        'syncid': {
                            'type': 'long'
                        },
                        'creator': {
                            'fielddata':'true',
                            "type": "text",
                            "store": "no",
                            "term_vector": "with_positions_offsets",
                            "analyzer": "ik_smart",
                            "search_analyzer": "ik_max_word",
                            "boost": 8
                        },
                        'age': {
                            'type': 'long'
                        },
                        'agegroup':{
                            'type': 'text'
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'answer': {
                            "type": "text",
                            "store": "no",
                            "term_vector": "with_positions_offsets",
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_max_word",
                            "boost": 8
                        },
                        'guid': {
                            'type': 'text'
                        },
                        'isdel': {
                            'type': 'long'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'guid': {
                    'fielddata':'true',
                    'type': 'text'
                },
                'scene-guid': {
                    'type': 'text',
                    "fielddata": 'true'
                },
                'editor': {
                    'type': 'text'
                },
                'isdel': {
                    'type': 'long'
                },
                'hasque': {
                    'type': 'long'
                },
                'corpus': {
                    'type':'nested',
                    'properties': {
                        'creator': {
                            'type': 'text'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'corpusid': {
                            'type': 'text'
                        },
                        'dsc': {
                            'type': 'text'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'createtime': {
                    'type': 'long'
                },
                'edittime': {
                    'type': 'long'
                }
            }
        }
    }
}


mc = {
    'mappings': {
        'corpus': {
            'properties': {
                'guid': {
                    'type': 'text'
                },
                'dsc': {
                    "type": "text",
                    "store": "no",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_smart",
                    "search_analyzer": "ik_max_word",
                    "boost": 8
                },
                'creator': {
                    'type': 'text'
                },
                'editor': {
                    'type': 'text'
                },
                'createtime': {
                    'type': 'long'
                },
                'edittime': {
                    'type': 'long'
                },
                'syncid':{
                    'type':'long'
                }
            }
        }
    }
}

md = {
    'mappings':{
        'sscn': {
            'properties': {
                'ename': {
                    'type': 'text'
                },
                'isabled': {
                    'type': 'long'
                },
                'name': {
                    'type': 'text'
                },
                'editor': {
                    'type': 'text'
                },
                'guid': {
                    'type': 'text',
                    'fielddata':'true'
                },
                'fsid': {
                    'type': 'text'
                },
                'isdel': {
                    'type': 'long'
                },
                'dsc': {
                    'type': 'text'
                },
                'group-count':{
                    'type':'long'
                },
                'syncid':{
                    'type':'long'
                }
            }
        }
    }
}

me = {
    'mappings': {
        'grouprd': {
            'properties': {
                'isabled': {
                    'type': 'long'
                },
                'scene': {
                    'type': 'text'
                },
                'creator': {
                    'type': 'text'
                },
                'syncid': {
                    'type': 'long'
                },
                'allque': {
                    'properties': {
                        'creator': {
                            'type': 'text'
                        },
                        'guid': {
                            'type': 'text'
                        },
                        'syncid': {
                            'type': 'long'
                        },
                        'question': {
                            "type": "text"
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'keywords': {
                            "type": "text"
                        },
                        'isdel': {
                            'type': 'long'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'fscene-guid': {
                    'type': 'text'
                },
                'allans': {
                    'properties': {
                        'isabled': {
                            'type': 'long'
                        },
                        'weight': {
                            'type': 'long'
                        },
                        'syncid': {
                            'type': 'long'
                        },
                        'creator': {
                            'type': 'text'
                        },
                        'age': {
                            'type': 'long'
                        },
                        'agegroup':{
                            'type': 'text'
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'answer': {
                            "type": "text"
                        },
                        'guid': {
                            'type': 'text'
                        },
                        'isdel': {
                            'type': 'long'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'guid': {
                    'fielddata':'true',
                    'type': 'text'
                },
                'scene-guid': {
                    'type': 'text',
                    "fielddata": 'true'
                },
                'editor': {
                    'type': 'text'
                },
                'isdel': {
                    'type': 'long'
                },
                'hasque': {
                    'type': 'long'
                },
                'corpus': {
                    'properties': {
                        'creator': {
                            'type': 'text'
                        },
                        'createtime': {
                            'type': 'long'
                        },
                        'editor': {
                            'type': 'text'
                        },
                        'corpusid': {
                            'type': 'text'
                        },
                        'dsc': {
                            'type': 'text'
                        },
                        'edittime': {
                            'type': 'long'
                        }
                    }
                },
                'createtime': {
                    'type': 'long'
                },
                'edittime': {
                    'type': 'long'
                }
            }
        }
    }
}

mf = {
    "mappings":{
        "record":{
            "properties":{
                "date":{
                    "type":'long'
                },
                "corpusid":{
                    'fielddata':'true',
                    "type": "text"
                },
                "editor":{
                    'fielddata':'true',
                    "type": "text",
                    "store": "no",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_smart",
                    "search_analyzer": "ik_max_word",
                },
                "corpus":{
                    'fielddata':'true',
                    "type": "text",
                    "store": "no",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_smart",
                    "search_analyzer": "ik_max_word",
                },
                "operatetype":{
                    "type":'text',
                    'fielddata':'true'
                },
                "count":{
                    "type":"long"
                },
                "ids":{
                    "type":"nested",
                    "properties":{
                        "guid":{
                            'type':'text',
                            'fielddata':'true'
                        }
                    }
                }
            }
        }
    }
}

# maa = {
#     "action":[
#         {
#             "add":{
#                 "index":"scene-index",
#                 "alias":"si"
#             }
#         }
#     ]
# }

# res = es.indices.delete_alias(index='fscene-index', name='fi')
# print(res)

# res = es.indices.delete(index='fscene-index')
# print(res)

# res = es.indices.delete_alias(index='sscene-index', name='si')
# print(res)

# res = es.indices.delete(index='sscene-index')
# print(res)

# res = es.indices.delete_alias(index='corpus-index', name='ci')
# print(res)

# res = es.indices.delete(index='corpus-index')
# print(res)

# res = es.indices.delete_alias(index='group-index', name='gi')
# print(res)

# res = es.indices.delete(index='group-index')
# print(res)

# res = es.indices.create(index='fscene-index',body=ma)
# print(res)

# res = es.indices.put_alias(index='fscene-index', name='fi')
# print(res)

# res = es.indices.create(index='sscene-index',body=md)
# print(res)

# res = es.indices.put_alias(index='sscene-index', name='si')
# print(res)

# res = es.indices.create(index='group-index',body=mb)
# print(res)
 
# res = es.indices.put_alias(index='group-index', name='gi')
# print(res)

# res = es.indices.create(index='corpus-index',body=mc)
# print(res)

# res = es.indices.put_alias(index='corpus-index', name='ci')
# print(res)

# res = es.indices.create(index='group-record',body=me)
# print(res)
 
# res = es.indices.put_alias(index='group-record', name='gr')
# print(res)

# res = es.indices.delete_alias(index='record-index', name='ri')
# print(res)

# res = es.indices.delete(index='record-index')
# print(res)

# res = es.indices.create(index='record-index',body=mf)
# print(res)
 
# res = es.indices.put_alias(index='record-index', name='ri')
# print(res)


# 映射局部更新
# ma1 = {
#     'properties': {
#         'ss': {
#             'properties': {
#                 'ename': {
#                     'type': 'text'
#                 },
#                 'isabled': {
#                     'type': 'long'
#                 },
#                 'name': {
#                     'type': 'text'
#                 },
#                 'editor': {
#                     'type': 'text'
#                 },
#                 'sid': {
#                     'type': 'text',
#                     'fielddata':'true'
#                 },
#                 'isdel': {
#                     'type': 'long'
#                 },
#                 'dsc': {
#                     'type': 'text'
#                 }
#             }
#         }
#     }
# }

# ma2 = {
#     'properties':{
#         "id":{
#             'type':'text',
#             'fielddata':'true'
#         }
#     }
# }

md1 = {
    'properties':{
        "fsid":{
            'type':'text'
        }
    }
}

# res = es.indices.put_mapping(doc_type='sscn',body=md1,index='si')
# print(json.dumps(res, ensure_ascii=False))

# param = {
#     "query" : { 
#         "multi_match" : {
#             "query":"裙子穿",
#             "operator":"and",
#             "fields":["allque.question","allans.answer"]
#         } 
#     }
# }

# res = es.search(index="group-index", body=param)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(json.dumps(res,ensure_ascii=False))
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# for hit in res['hits']['hits']:
# 	# print(hit["_source"])
#     data = hit["_source"]
#     ql = data["allque"]
#     al = data["allans"]
#     que = ql[0]
#     ans = al[0]
#     print(que["question"])
#     print(ans["answer"])

# res = es.get(index="group-index", doc_type='group', id='3b379d14-a9f0-474e-8ff2-5e97b06a0b97')
# print(res['_source'])

# param = {
#     "query":{
#         "multi_match":{
#             "query":0,
#             "operator":"and",
#             "fields":["isdel", "ss.isdel"]
#         }
#     }
# }

# param = {
#     "size":500,
#     "_source":["ename","name","id","ss.ename","ss.sid","ss.name"],
#     "query":{
#         "match":{
#             "isdel":0
#         },
#         "match":{
#             "ss.isdel":0
#         }
#     }
# }

# res = es.search(index="scene-index", body=param)
# print(json.dumps(res,ensure_ascii=False))
# print(res)
# for hit in res['hits']['hits']:
	# print(hit["_source"])
    # print(">>>> ")
    # # ql = hit["ss"]
    # que = ql[0]
    # print(que["question"])


mf1 = {
    'properties':{
        "add":{
            "type":"nested",
            "properties":{
                "guid":{
                    'type':'text',
                    'fielddata':'true'
                }
            }
        },
        "del":{
            "type":"nested",
            "properties":{
                "guid":{
                    'type':'text',
                    'fielddata':'true'
                }
            }
        },
        "update":{
            "type":"nested",
            "properties":{
                "guid":{
                    'type':'text',
                    'fielddata':'true'
                }
            }
        },
        "enable":{
            "type":"nested",
            "properties":{
                "guid":{
                    'type':'text',
                    'fielddata':'true'
                }
            }
        },
        "disable":{
            "type":"nested",
            "properties":{
                "guid":{
                    'type':'text',
                    'fielddata':'true'
                }
            }
        }
    }
}

mf2 = {
    'properties':{
        'count':{
            'type':'long'
        }
    }
}

# res = es.indices.put_mapping(index='ri', doc_type='record', body=mf2)
# print res

# res = es.flush()

# res = es.indices.get_mapping(doc_type='record',index='ri')
# print res