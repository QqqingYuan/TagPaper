# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

from word2vec import model_util
import redis
import numpy as np
from word2vec import score
from collections import defaultdict
from sklearn.metrics import recall_score,accuracy_score,f1_score

# redis
r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)


def get_vector(word):
    result = r.get(word)
    if result is not None:
        vec = np.fromstring(result,dtype=np.float32)
    else:
        vec = None
    return vec


all_class_centers = ['建筑','机械','计算机']
centers = model_util.get_center_embeddings(all_class_centers)


def get_class_score(word):
    w_v = get_vector(word)
    if w_v is None:
        return None
    distances = []
    for idx,center in enumerate(centers):
        center_dis = np.linalg.norm(w_v - center)
        distances.append((idx,center_dis))

    dis_sorted = sorted(distances,key= lambda pair:pair[1])
    # TODO: select related areas
    selected_dis = dis_sorted[:3]
    idxs = []
    top_dis = []
    for pair in selected_dis:
        idxs.append(pair[0])
        top_dis.append(pair[1])
    final_scores = score.class_score(top_dis)
    return [(x,y) for x,y in zip(idxs,final_scores)]


def predict_class(keywords):
    # keywords = keywords_str.split()
    record = defaultdict(float)
    for keyword in keywords:
        scores = get_class_score(keyword)
        if scores is None:
            continue
        # TODO: add weight for keyword
        for item in scores:
            record[item[0]] += item[1]
    """
    # print result
    for key in record:
        print(str(all_class_centers[key])+" "+str(record[key]))
    """
    predict_sort = sorted(record.items(), key=lambda d:d[1], reverse = True)
    return predict_sort[0][0]


texts, labels = model_util.load_text_label()

pred_labels = []
count = 0
for text in texts:
    label = predict_class(text)
    pred_labels.append(label)
    count += 1


# compute accuracy
acc = accuracy_score(labels,pred_labels)
recall = recall_score(labels,pred_labels,average='macro')
f1 = f1_score(labels,pred_labels,average='macro')
print("accuracy: "+str(acc))
print("recall: "+str(recall))
print("F1:"+str(f1))
