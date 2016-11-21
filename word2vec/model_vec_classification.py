# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
import redis
import numpy as np
from collections import defaultdict
from word2vec import model_util
from sklearn.svm import SVC,LinearSVC

word_embedding_size = model_util.word_embedding_size


def get_tfidf_top(tfidf_corpus,top_number):
    top_corpus = []
    for doc in tfidf_corpus:
        # from small to large
        doc_sorted = sorted(doc,key= lambda pair:pair[1])
        top_corpus.append(doc_sorted[-top_number:])
    return top_corpus


# random init a 200-dim vector
def getRandom_vec():
    vec=np.random.rand(word_embedding_size)
    norm=np.sum(vec**2)**0.5
    normalized = vec / norm
    return normalized


def get_dic_embeddings(words_dic):
    # redis
    r = redis.StrictRedis(host='10.2.1.7', port=6379, db=0)
    count = 0
    embeddings_dic = defaultdict()
    for i in words_dic:
        line = words_dic[i].strip('\n').strip()
        result = r.get(line)
        if result is not None:
            vec = np.fromstring(result,dtype=np.float32)
            embeddings_dic[i] = vec
        else:
            count += 1
            embeddings_dic[i] = getRandom_vec()
    # print(count)
    return embeddings_dic


corpus,dic,labels = load_data.load_corpus()
# TF-IDF
tfidf = gensim.models.TfidfModel(corpus=corpus,dictionary=dic)
# corpus_tfidf = [tfidf[doc] for doc in corpus]
corpus_tfidf = tfidf[corpus]
corpus_top = get_tfidf_top(corpus_tfidf,top_number=10)

dic_embeddings = get_dic_embeddings(dic)
doc_embeddings = model_util.get_doc_embeddings(corpus_top,dic_embeddings)
train_data,train_label,test_data,test_label = load_data.get_train_test(doc_embeddings,labels)
print(train_data.shape)

clf = LinearSVC()
clf.fit(train_data,train_label)
score = clf.score(test_data,test_label)
print(score)



