# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import numpy as np
import redis


word_embedding_size = 200


# compute sum doc embeddings with TF-IDF weight
def get_doc_embeddings(corpus_top,embeddings):
    size = len(corpus_top)
    doc_embeddings = np.zeros(shape=(size,word_embedding_size),dtype=np.float32)
    count = 0
    for doc in corpus_top:
        doc_sum = 0
        for pair in doc:
            word = embeddings[pair[0]]
            weight = pair[1]
            doc_sum += word * weight
        doc_embeddings[count] = doc_sum
        count += 1
    return doc_embeddings


# compute average doc embeddings
def get_average_doc_embeddings(corpus_top,embeddings):
    size = len(corpus_top)
    doc_embeddings = np.zeros(shape=(size,word_embedding_size),dtype=np.float32)
    count = 0
    for doc in corpus_top:
        length = len(doc)
        doc_sum = 0
        for pair in doc:
            word = embeddings[pair[0]]
            doc_sum += word
        doc_embeddings[count] = doc_sum / length
        count += 1
    return doc_embeddings


# compute doc 's predicted classes
def doc_pred(doc,centers):
    min_dis = -1
    target_label = -1
    for idx,center in enumerate(centers):
        center_dis = np.linalg.norm(doc - center)
        if min_dis == -1 :
            min_dis = center_dis
            target_label = idx
        else:
            if center_dis < min_dis:
                min_dis = center_dis
                target_label = idx

    return target_label


# compute distance between doc embeddings and clustering center , return predicted class
def clustering_pred(doc_embeddings,centers):
    pred_labels = []
    for doc in doc_embeddings:
        pred_labels.append(doc_pred(doc,centers))
    return pred_labels


# get center embeddings
def get_center_embeddings(words):
    # redis
    r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)
    words_embeddings = []
    for word in words:
        result = r.get(word)
        if result is not None:
            vec = np.fromstring(result,dtype=np.float32)
            words_embeddings.append(vec)
        else:
            print(word + ' 获取不到!')
    return words_embeddings


# [心理，机械，计算机，建筑]
def read_centers(file):
    centers = np.load(file)
    return centers
