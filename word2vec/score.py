__author__ = 'PC-LiNing'

import numpy as np


def softmax_score(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def transform(base, delta, l, r_,):
    return np.exp((l-delta)/(r_*base))


def class_score(scores):
    r = 0.2
    base = scores[0]
    scores_delta = [score-base for score in scores]
    L = scores_delta[-1]
    scores_final = [transform(base,delta,L,r) for delta in scores_delta]
    return softmax_score(scores_final)


# print(class_score([3.36,3.86,4.12]))
