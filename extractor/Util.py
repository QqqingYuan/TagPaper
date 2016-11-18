# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import jieba
import re


# filter
def SentFilter(sent):
    filtrate = re.compile(u'[^\u4E00-\u9FA5]')
    filtered_str = filtrate.sub(r'', sent)
    return filtered_str


# segment
def SegSentence(sent):
    seg_list = jieba.cut(SentFilter(sent))
    return " ".join(seg_list)+"\n"


