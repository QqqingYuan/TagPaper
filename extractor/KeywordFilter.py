# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs
import re

def filter(sentence, frequency):
    # filter illegal character
    exclude = ['(',')','@','&','、','/','”','“','～','*','=',';','】','【','[',']','?']
    for one in exclude:
        if one in sentence:
            return False
    # filter number
    if sentence.isdigit():
        return False
    # length limit
    if len(sentence) == 1:
        return False
    if len(sentence) > 10 and frequency < 10 :
        return False
    if frequency < 5 :
        filtrate = re.compile(u'[^\u4E00-\u9FA5]')
        filtered_str = filtrate.sub(r'', sentence)
        if len(filtered_str) != len(sentence):
            return False
    return True


f = codecs.open("keywordrank.txt",encoding='utf-8')
output = codecs.open("keywords.txt","a",encoding='utf-8')
error = codecs.open("error.txt","a",encoding='utf-8')
excep = codecs.open("excep.txt","a",encoding='utf-8')
count = 0
for line in f.readlines():
    line = line.strip('\n').strip()
    temp = line.split(' ')
    if len(temp) != 2:
        print("error => {:g} .".format(count))
        count += 1
        excep.write(line+'\n')
        continue
    word,frequency = temp[0],temp[1]
    if filter(word,int(frequency)):
        output.write(word+'\n')
    else:
        error.write(word+'\n')
    count += 1

f.close()
output.close()
error.close()
excep.close()