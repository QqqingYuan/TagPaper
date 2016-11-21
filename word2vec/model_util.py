# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import numpy as np

word_embedding_size = 200


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


