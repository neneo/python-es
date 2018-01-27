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
        # "size":0,
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
                            "fscene-guid":"ab0817728e224a1ab87a49e50cba9fb2"
                        }
                    },
                    {
                        "term":{
                            "scene-guid":"3de2fa188d7245e68b7c54e55b9de73d"
                        }
                    },
                    {
                        "nested":{
                            "path":"corpus",
                            "query":{
                                "terms":{
                                    "corpus.corpusid":["3574d30acb6d450c92e82ef4b0297063", "ffe4d66da298451aa4685121dbcfa981", "efbade5e514f4011866c35db6e0c55ca", "3f36b0ed26cb4cc894549bad0c86dfe2"]
                                }
                            }
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
                                                "allans.agegroup":'4'
                                            }
                                        },
                                        {
                                            "term":{
                                                "allans.weight":7   
                                            }
                                        },
                                        {
                                            "match":{
                                                "allans.creator":"管理员"
                                            }
                                        },
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
                        "nested":{
                            "path":"allans",
                            "query":{
                                "match":{
                                    "allans.answer":"可爱 亲爱"
                                }
                            }
                        }
                    },
                    {
                        "nested":{
                            "path":"allque",
                            "query":{
                                "bool":{
                                    "should":[
                                        {
                                            "match":{
                                                "allque.question":"可爱 亲爱"
                                            }
                                        },
                                        {
                                            "match":{
                                                "allque.keywords":"可爱 亲爱"
                                            }
                                        }
                                    ],
                                    "minimum_should_match":1
                                }
                            }
                        }
                    }
                ],
                "minimum_should_match":1
            }
        }#,
        # "aggs":{
        #     "groupcount":{
        #         "cardinality":{
        #             "field":"guid"
        #         }
        #     }
        # }
    }


    # param = {
    #     "query":{
    #         "bool":{
    #             "should":[
    #                 {
    #                     "nested":{
    #                         "path":"allans",
    #                         "query":{
    #                             "terms":{
    #                                 "allans.answer":["开爱"]
    #                             }
    #                         }
    #                     }
    #                 },
    #                 {
    #                     "nested":{
    #                         "path":"allque",
    #                         "query":{
    #                             "terms":{
    #                                 "allque.question":["可爱"]
    #                             }
    #                         }
    #                     }
    #                 }
    #             ],
    #             "minimum_should_match":1
    #         }
    #     }
    # }

    param = {
        "query":{
            "bool":{
                "should":[
                    {
                        "bool":{
                            "minimum_should_match":1,
                            "must":[
                                {
                                    "term":{
                                        "isdel":0
                                    }
                                },
                                {
                                    "term":{
                                        "hasque":1
                                    }
                                },
                                {
                                    "term":{
                                        "scene-guid":"247bef1054484863a07a3576dbbd2649"
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"corpus",
                                        "query":{
                                            "terms":{
                                                "corpus.corpusid":["3574d30acb6d450c92e82ef4b0297063","ffe4d66da298451aa4685121dbcfa981","efbade5e514f4011866c35db6e0c55ca","3f36b0ed26cb4cc894549bad0c86dfe2"]
                                            }
                                        }
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allans",
                                        "query":{
                                            "bool":{
                                                "must":[
                                                    # {
                                                    #     "term":{
                                                    #         "allans.weight":7
                                                    #     }
                                                    # },
                                                    # {
                                                    #     "term":{
                                                    #         "allans.agegroup":"4"
                                                    #     }
                                                    # },
                                                    {
                                                        "term":{
                                                            "allans.isdel":0
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allque",
                                        "query":{
                                            "term":{
                                                "allque.isdel":1
                                            }
                                        }
                                    }
                                }
                            ],
                            "should":[
                                {
                                    "nested":{
                                        "path":"allans",
                                        "query":{
                                            "match":{
                                                "allans.answer":"早上"
                                            }
                                        }
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allque",
                                        "query":{
                                            "bool":{
                                                "minimum_should_match":1,
                                                "should":[
                                                    {
                                                        "match":{
                                                            "allque.question":"早上"
                                                        }
                                                    },
                                                    {
                                                        "match":{
                                                            "allque.keywords":"早上"
                                                        }
                                                    }
                                                ]
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
                                        "isdel":0
                                    }
                                },
                                {
                                    "term":{
                                        "hasque":0
                                    }
                                },
                                {
                                    "term":{
                                        "scene-guid":"247bef1054484863a07a3576dbbd2649"
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"corpus",
                                        "query":{
                                            "terms":{
                                                "corpus.corpusid":["3574d30acb6d450c92e82ef4b0297063","ffe4d66da298451aa4685121dbcfa981","efbade5e514f4011866c35db6e0c55ca","3f36b0ed26cb4cc894549bad0c86dfe2"]
                                            }
                                        }
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allans",
                                        "query":{
                                            "bool":{
                                                "must":[
                                                    # {
                                                    #     "term":{
                                                    #         "allans.weight":7
                                                    #     }
                                                    # },
                                                    # {
                                                    #     "term":{
                                                    #         "allans.agegroup":"4"
                                                    #     }
                                                    # },
                                                    {
                                                        "term":{
                                                            "allans.isdel":0
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                },
                                {
                                    "nested":{
                                        "path":"allans",
                                        "query":{
                                            "match":{
                                                "allans.answer":"早上"
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ],
                "minimum_should_match":1,

                # "must_not":{
                #     "bool":{
                #         "must":[
                #             {
                #                 "term":{
                #                     "hasque":1
                #                 }
                #             },
                #             {
                #                 "nested":{
                #                     "path":"allque",
                #                     "query":{
                #                         "term":{
                #                             "allque.isdel":0
                #                         }
                #                     }
                #                 }
                #             }
                #         ]
                #     }
                # }
            }
        },
        "size":1000
    }

    param = {
        "_source":[
            "scene-guid",
            "allque",
            "allans"
        ],
        "query":{
            "term":{
                "hasque":0
            }
        }
    }


    res = es.search(index='gi', body=param)
    print(json.dumps(res, ensure_ascii=False))