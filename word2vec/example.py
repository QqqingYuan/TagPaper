# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import numpy as np
import redis

# redis
r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)

word = '中国'
vec = np.fromstring(r.get(word),dtype=np.float32)
print(vec)
