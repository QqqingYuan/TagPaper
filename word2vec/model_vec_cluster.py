# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
import redis
import numpy as np
from collections import defaultdict
from word2vec import model_util
from sklearn.metrics import recall_score,accuracy_score,f1_score

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
corpus_tfidf = tfidf[corpus]
corpus_top = get_tfidf_top(corpus_tfidf,top_number=10)


dic_embeddings = get_dic_embeddings(dic)

doc_embeddings = model_util.get_average_doc_embeddings(corpus_top,dic_embeddings)

# shuffle data
shuffle_indices = np.random.permutation(np.arange(len(corpus_top)))
labels_shuffled = labels[shuffle_indices]
doc_embeddings_shuffled = doc_embeddings[shuffle_indices]

# centers
four_class_centers = ['建筑','机械','计算机']
centers = model_util.get_center_embeddings(four_class_centers)
# four_class_centers = model_util.read_centers('centroids.npy')
# centers = [four_class_centers[3],four_class_centers[0],four_class_centers[1],four_class_centers[2]]

# predict
pred_labels = model_util.clustering_pred(doc_embeddings_shuffled,centers=centers)
# compute accuracy
acc = accuracy_score(labels_shuffled,pred_labels)
recall = recall_score(labels_shuffled,pred_labels,average='macro')
f1 = f1_score(labels_shuffled,pred_labels,average='macro')
print(acc)
print(recall)
print(f1)





