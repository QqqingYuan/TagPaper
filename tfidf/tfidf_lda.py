# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim
from lda import load_data
import numpy as np
from sklearn.lda import LDA

corpus,dic,labels = load_data.load_corpus()
tfidf = gensim.models.TfidfModel(corpus=corpus,dictionary=dic)
corpus_tfidf = [tfidf[doc] for doc in corpus]

matrix = load_data.convert_to_matrix(corpus_tfidf)
train_data,train_label,test_data,test_label = load_data.get_train_test(matrix,labels)

lda = LDA(solver='svd',store_covariance=True)
lda.fit(train_data,train_label)
score = lda.score(test_data,test_label)
print(score)




