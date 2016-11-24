# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

from word2vec import model_util
import redis
import numpy as np
from word2vec import score
from collections import defaultdict


def get_vector(word):
    # redis
    r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)
    result = r.get(word)
    if result is not None:
        vec = np.fromstring(result,dtype=np.float32)
    else:
        vec =None
    return vec


all_class_centers = ['建筑','机械','计算机','化学','物理','数学','地理','经济','法律','天文']
centers = model_util.get_center_embeddings(all_class_centers)


def get_class_score(word):
    w_v = get_vector(word)
    distances = []
    for idx,center in enumerate(centers):
        center_dis = np.linalg.norm(w_v - center)
        distances.append((idx,center_dis))

    dis_sorted = sorted(distances,key= lambda pair:pair[1])
    selected_dis = dis_sorted[:3]
    idxs = []
    top_dis = []
    for pair in selected_dis:
        idxs.append(pair[0])
        top_dis.append(pair[1])
    final_scores = score.class_score(top_dis)
    return [(x,y) for x,y in zip(idxs,final_scores)]


keywords_str = '辅助 诊断系统 脑电波 生物 数据库 数据库 结构'
keywords = keywords_str.split()

record = defaultdict(float)
for keyword in keywords:
    scores = get_class_score(keyword)
    # TODO: add weight for keyword
    for item in scores:
        record[item[0]] += item[1]

# print result
for key in record:
    print(str(all_class_centers[key])+" "+str(record[key]))



