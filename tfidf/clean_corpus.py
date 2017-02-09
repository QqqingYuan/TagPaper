# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs
from gensim import corpora
import numpy as np
from collections import defaultdict
import pickle
import datetime


def filter_single_word(file):
    # line total
    # total = 13924390
    total = 14862090
    f = open(file)
    output = codecs.open("all_single_word.txt","a",encoding='utf-8')
    frequency = defaultdict(int)
    count = 0
    # read with cache
    while 1:
        lines = f.readlines(100000)
        if not lines:
            break
        for line in lines:
            line = line.strip('\n').strip()
            words = line.split()
            # remove stop word and single word
            text = [word for word in words if len(word) > 1]
            output.write(" ".join(text)+'\n')
            # remove words that appear only once
            for token in text:
                frequency[token] += 1
            count += 1
            if count % 10000 == 0:
                time_str = datetime.datetime.now().isoformat()
                process = count / total * 100
                print("{}: processed {:g} % , already processed {:g} texts.".format(time_str,process,count))

    print("dict size : "+str(len(frequency)))
    # save frequency
    fre_dict = open("fre_dict","wb")
    pickle.dump(frequency,fre_dict)
    f.close()
    output.close()
    fre_dict.close()


def reduce_frequency(file):
    # line total
    # total = 13924390
    total = 14862090
    f = open(file)
    output = codecs.open("all_reduce_frequency.txt","a",encoding='utf-8')
    fre = open("fre_dict","rb")
    frequency = pickle.load(fre)
    count = 0
    # read with cache
    while 1:
        lines = f.readlines(100000)
        if not lines:
            break
        for line in lines:
            line = line.strip('\n').strip()
            text = line.split()
            # remove words that appear only once
            text = [token for token in text if frequency[token] > 1]
            output.write(" ".join(text)+'\n')
            count += 1
            if count % 10000 == 0:
                time_str = datetime.datetime.now().isoformat()
                process = count / total * 100
                print("{}: processed {:g} % , already processed {:g} texts.".format(time_str,process,count))

    f.close()
    output.close()

# clean corpus
filter_single_word('all_seg.txt')
reduce_frequency("all_single_word.txt")