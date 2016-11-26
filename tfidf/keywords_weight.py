# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
import numpy as np
from word2vec import model_util
import redis


def degree_diff(word,centers):
    distances = []
    word_vec = get_vector(word)
    if word_vec is None:
        return None
    for center in centers:
        distances.append(np.linalg.norm(word_vec - center))
    return np.var(np.asarray(distances))

# redis
r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)


def get_vector(word):
    result = r.get(word)
    if result is not None:
        vec = np.fromstring(result,dtype=np.float32)
    else:
        vec = None
    return vec

corpus,dic,labels = load_data.load_corpus()
tfidf = gensim.models.TfidfModel(corpus=corpus,dictionary=dic)
corpus_tfidf = [tfidf[doc] for doc in corpus]

all_class_centers = ['建筑','机械','计算机']
centers = model_util.get_center_embeddings(all_class_centers)

paper = corpus_tfidf[100]
allwords = [dic[pair[0]] for pair in paper]
print(allwords)
doc_sorted = sorted(paper,key= lambda pair:pair[1])
# select top 10
keywords = doc_sorted[-10:]
print('top 10 word and tf-idf: ')
for word in keywords:
    print(dic[word[0]]+" "+str(word[1]))

print('#######')

print('keyword and degree-diff: ')

for word in keywords:
    current = dic[word[0]]
    print(current+" " + str(degree_diff(current,centers)))




