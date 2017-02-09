# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs
import re


def filter(sentence, frequency):
    # length limit
    if len(sentence) == 1:
        return False

    return True


f = codecs.open("all_keywords",encoding='utf-8')
output = codecs.open("all_keywords.txt","a",encoding='utf-8')
count = 0
for line in f.readlines():
    line = line.strip('\n').strip()
    temp = line.split(' ')
    if len(temp) != 2:
        print("error => {:g} .".format(count))
        count += 1
        continue
    word,frequency = temp[0],temp[1]
    if filter(word,int(frequency)):
        output.write(word+'\n')
    count += 1

f.close()
output.close()
