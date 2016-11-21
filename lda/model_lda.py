# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
import numpy as np
from sklearn.svm import SVC,LinearSVC


def get_corpus_topic_distribution(topics_corpus, num_topic):
    matrix = np.zeros(shape=(len(topics_corpus),num_topic),dtype=np.float32)
    count = 0
    for line in topics_corpus:
        row = np.asarray([pair[1] for pair in line],dtype=np.float32)
        matrix[count] = row
        count += 1
    return matrix


corpus,dic,labels = load_data.load_corpus()
lda_model = gensim.models.LdaModel(corpus,num_topics=3,id2word=dic)

doc_topics = []
for doc in corpus:
    doc_topics.append(lda_model.get_document_topics(doc,minimum_probability=0))

doc_topics_matrix = get_corpus_topic_distribution(doc_topics,num_topic=3)
train_data,train_label,test_data,test_label = load_data.get_train_test(doc_topics_matrix,labels)
print(train_data.shape)

# SVM classification
# clf = SVC()
clf = LinearSVC()
clf.fit(train_data,train_label)
score = clf.score(test_data,test_label)
print(score)
