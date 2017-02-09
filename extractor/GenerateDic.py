# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs

f = codecs.open("all_keywords.txt",encoding='utf-8')
dic = codecs.open("all_keywords.dic","a",encoding='utf-8')

count = 0
for line in f.readlines():
    line = line.strip('\n').strip()
    new_line = line + "	user_define	8"
    dic.write(new_line+'\n')
    count += 1

f.close()
dic.close()