# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs
import re

def SentFilter(sent):
    filtrate = re.compile(u'[^\u4E00-\u9FA5]')
    filtered_str = filtrate.sub(r'', sent)
    return filtered_str

f = codecs.open("field_words",'a',encoding='utf-8')
dic = codecs.open("addition.dic",encoding='utf-8')

count = 0
for line in dic.readlines():
    line = line.strip('\n').strip()
    word = SentFilter(line)
    f.write(word+'\n')
    count += 1

f.close()
dic.close()