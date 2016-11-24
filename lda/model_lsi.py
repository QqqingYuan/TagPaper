# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
from sklearn.lda import LDA
import numpy as np
from sklearn.svm import LinearSVC


def get_corpus_topic_distribution(topics_corpus, num_topic):
    matrix = np.zeros(shape=(len(topics_corpus),num_topic),dtype=np.float32)
    count = 0
    for line in topics_corpus:
        row = np.asarray([pair[1] for pair in line],dtype=np.float32)
        try:
            matrix[count] = row
        except ValueError:
            print(count)
        count += 1
    return matrix

corpus,dic,labels = load_data.load_corpus()

# TF-IDF
tfidf = gensim.models.TfidfModel(corpus=corpus,dictionary=dic)
# corpus_tfidf = [tfidf[doc] for doc in corpus]
corpus_tfidf = tfidf[corpus]

# LSI
lsi_model = gensim.models.LsiModel(corpus_tfidf,num_topics=4,id2word=dic)

doc_topics = []
for doc in corpus_tfidf:
    doc_topics.append(lsi_model[doc])

doc_topics_matrix = get_corpus_topic_distribution(doc_topics,num_topic=4)
train_data,train_label,test_data,test_label = load_data.get_train_test(doc_topics_matrix,labels)
print("train size: "+str(train_data.shape[0]))
print("test size: "+str(test_data.shape[0]))

# SVM classification
# clf = SVC()
clf = LinearSVC()
clf.fit(train_data,train_label)
score = clf.score(test_data,test_label)
print(score)


