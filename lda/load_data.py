# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs
from gensim import corpora
from scipy import sparse
import numpy as np
from collections import defaultdict

stoplist = set('的 和 与 中 为 及 对 在 了 例'.split())


def load_texts(file):
    f = codecs.open(file,encoding='utf-8')
    texts = []
    for line in f.readlines():
        line = line.strip('\n').strip()
        words = line.split()
        # remove stop word and single word
        texts.append([word for word in words if word not in stoplist and len(word) > 1])
    return texts


def load_corpus():
    texts_1 = load_texts('F:/PycharmProjects/TagPaper/lda/result_1')
    texts_2 = load_texts('F:/PycharmProjects/TagPaper/lda/result_2')
    texts_3 = load_texts('F:/PycharmProjects/TagPaper/lda/result_3')
    tag_list = [0]*len(texts_1) + [1]*len(texts_2) + [2]*len(texts_3)
    texts = texts_1 + texts_2 + texts_3
    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus,dictionary,np.asarray(tag_list)


def get_max_length(corpus):
    max_length = 0
    for line in corpus:
        if len(line) > max_length:
            max_length = len(line)
    return max_length


def convert_to_matrix(corpus):
    max_length = get_max_length(corpus)
    print('max length : '+str(max_length))
    matrix = np.zeros(shape=(len(corpus),max_length),dtype=np.int32)
    count = 0
    for line in corpus:
        row = np.asarray([pair[0] for pair in line]+[-1]*(max_length-len(line)),dtype=np.int32)
        matrix[count] = row
        count += 1
    return matrix


def get_train_test(matrix,tag_list):
    line_count = len(tag_list)
    shuffle_indices = np.random.permutation(np.arange(line_count))
    label_shuffled = tag_list[shuffle_indices]
    matrix_shuffled = matrix[shuffle_indices]
    Test_Size = line_count * 0.2
    x_train = matrix_shuffled[Test_Size:]
    y_train = label_shuffled[Test_Size:]
    x_test=matrix_shuffled[:Test_Size]
    y_test=label_shuffled[:Test_Size]
    return x_train,y_train,x_test,y_test


# load_corpus()
