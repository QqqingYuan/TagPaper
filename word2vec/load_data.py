# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import numpy as np
import redis


def  getEmbedding_Label():
    # redis
    r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)
    f = open("keywords/keywords","r")
    lines = f.readlines()
    number = 500
    count = 0
    EMBEDDING_SIZE = 200
    words = []
    embeddings = np.ndarray(shape=(number,EMBEDDING_SIZE),dtype=np.float32)
    for line in lines:
        line = line.strip('\n').strip()
        print(line)
        result = r.get(line)
        if result is not None:
            vec = np.fromstring(result,dtype=np.float32)
            words.append(line)
            embeddings[count] = vec
            count += 1
        else:
            print("skip")
            continue

        if count == number :
            break

    for word in words:
        print(word)

    return words,embeddings


