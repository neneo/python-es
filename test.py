#!/bin/bash/python3
#-*- coding:utf-8 -*-

from elasticsearch.exceptions import TransportError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://0.0.0.0:9200")


# index_data = {
#     "settings" : {
#         "number_of_shards" : 1
#     },
#     "mappings" : {
#         "test-index" : {
#             "properties" : {
#                 "id" : { "type" : "long", "store":"yes", "precision_step":"0" },
#                 "author":{ "type" : "string", "store":"no", "index":"analyzed" },
#                 "text" : { "type" : "string", "store":"no", "index":"analyzed" },
#                 "timestamp" : {"type" : "date", "store":"no", "index":"analyzed"}
#             }
#         }
#     }
# }

#res = es.indices.delete(index='test-index')
#print(res)

# res = es.indices.create(index='test-index',body=index_data)
# print(res)

# res = es.indices.close(index='my-index')
# print(res)

#timeofnow = datetime.now()

#doc = {
#    'author': '天行',
#    'text': 'Elasticsearch: cool. bonsai cool.',
#    'timestamp': timeofnow,
#}
#res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['created'])

#res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])

#es.indices.refresh(index="test-index")


res = es.search(index="fs-index", body={"query": {"match_all": {}}})
# res = es.search(index="test-index", body={"query": {'author':'天行'}})
#res = es.search(index="test-index", body={"query": {"match":{"author":"天行"}}})
# print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"])

print("---------------------")

# es.delete(index="test-index", doc_type="tweet", id=1)

# try:
#     res = es.get(index="test-index", doc_type='tweet', id=1)
#     print(res['_source'])
# except TransportError as e:
#     print(">>>>>>>>>>>>")
#     print(str(e))
#     print(">>>>>>>>>>>>")
