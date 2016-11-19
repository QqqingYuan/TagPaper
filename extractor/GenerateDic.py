# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import codecs

f = codecs.open("output",encoding='utf-8')
dic = codecs.open("keywords.dic","a",encoding='utf-8')

count = 0
for line in f.readlines():
    line = line.strip('\n').strip()
    temp = line.split(' ')
    if len(temp) != 2:
        print("error => {:g} .".format(count))
        count += 1
        continue
    new_line = temp[0] + "	user_define	8"
    dic.write(new_line+'\n')
    count += 1

f.close()
dic.close()