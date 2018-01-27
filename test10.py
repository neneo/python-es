#!/bin/bash/python
#-*- coding:utf-8 -*-

import time
import json
import requests

import sys
 

from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://10.172.98.150:9200")

def getTimeOClockOfToday():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S'))
    return long(time1)

if __name__ == '__main__':
    reload(sys)    
    sys.setdefaultencoding('utf8')

    param = {
        'query':{
            'match_all':{}
        }
    }

    param = {
        'query':{
            'bool':{
                'must':[
                    {
                        'match_all':{}
                    },
                    {
                        'range':{
                            'date':{
                                'gt':1504368000,
                                'lt':1504540800
                            }
                        }
                    }
                ]
            }
        }
    }

    res = es.search(index='ri', doc_type='record', body=param)
    print json.dumps(res)
    # print json.dumps(res, ensure_ascii=False)

    date = getTimeOClockOfToday()

    param = {
        'date':1504368000,
        'editor':'管理员',
        'corpus':'xiaoq',
        'count':0,
        'operatetype':'add',
        'ids':[]
    }

    # res = es.index(index='ri', doc_type='record', id="", body=param)
    # print json.dumps(res, ensure_ascii=False)

    param = {
        'date':date,
        'editor':'test',
        'corpus':'test',
        'count':0,
        'operatetype':'del',
        'ids':[]
    }


    # res = es.index(index='ri', doc_type='record', id="", body=param)
    # print json.dumps(res, ensure_ascii=False)

    # add 增加
    param = {
        'query':{
            'bool':{
                'must':[
                    {
                        'term':{
                            'date':date
                        }
                    },
                    {
                        'term':{
                            'editor':'test'
                        }
                    },
                    {
                        'term':{
                            'corpus':'test'
                        }
                    },
                    {
                        'term':{
                            'operatetype':'del'
                        }
                    }
                ]
            }
        },
        'script':{
            'inline':"ctx._source.count+=params.step;ctx._source.ids.add(params.data);",
            'lang':'painless',
            'params':{
                'step':1,
                'data':{
                    'guid':'123456005'
                }
            }
        }
    }
    # res = es.update_by_query(index='ri', doc_type='record', body=param)
    # print res
    # print json.dumps(res, ensure_ascii=False)

    param = {
        'query':{
            'bool':{
                'must':[
                    {
                        'term':{
                            'date':date
                        }
                    },
                    {
                        'term':{
                            'editor':'管理员'
                        }
                    },
                    {
                        'term':{
                            'corpus':'xiaoq'
                        }
                    },
                    {
                        'term':{
                            'operatetype':'add'
                        }
                    }
                ]
            }
        }
    }

    # param = {
    #     'query':{
    #         'match_all':{}
    #     }
    # }

    # res = es.search(index='ri', doc_type='record', body=param)
    # print json.dumps(res)

    param = {
        '_source':[
            'date',
            'editor',
            'corpus',
            'type'
        ],
        'query':{
            'match_all':{}
        },
        'aggs':{
            'idcount':{
                'nested':{
                    'path':'ids'
                },
                'aggs':{
                    'idsum':{
                        'sum':{
                            'field':'guid'
                        }
                    }
                }
            }
        }
    }

    # res = es.search(index='ri', doc_type='record', body=param)
    # print json.dumps(res)

    # res = es.get(index='ri', doc_type='record', id='AV48KYojcV_3Rrakfy8W')
    # print json.dumps(res, ensure_ascii=False)

    # res = requests.get('http://10.172.98.150:9200/ri/record/%s' % str(date))
    # print res.text

    # res = es.get(index="ri", doc_type="record", id="AV5Ll_vnkpcD2ZmNfDgh")
    # print res

    param = {
        'query':{
            'terms':{
                'corpus':['test', 'xiaoq']
            }
        }
    }

    res = es.search(index='ri', doc_type='record', body=param)
    print res