__author__ = 'PC-LiNing'

import codecs
import re


def SentFilter(sent):
    filtrate = re.compile(u'[^\u4E00-\u9FA5]')
    filtered_str = filtrate.sub(r'', sent)
    return filtered_str

f = codecs.open("error.txt",encoding='utf-8')
error = codecs.open("clean_error.txt","a",encoding='utf-8')
count = 0
for line in f.readlines():
    line = line.strip('\n').strip()
    temp = SentFilter(line)
    if temp is not '':
        error.write(temp+'\n')
    count += 1

f.close()
error.close()