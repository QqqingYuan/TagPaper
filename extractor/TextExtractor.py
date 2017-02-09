# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import pymysql
import datetime
import codecs
import re


def SentFilter(sent):
    filtrate = re.compile(u'[^\u4E00-\u9FA5]')
    filtered_str = filtrate.sub(r'', sent)
    return filtered_str

config = {
    'host':'10.2.1.57',
    'port':3306,
    'user':'root',
    'password':'1993',
    'db':'addition',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor
}

conn = pymysql.connect(**config)

contents = []
keywords = []
total_number = 1000
with conn.cursor() as cursor:
    category = 'zhexue'
    sql = 'select title,brief,keywords from '+category+'content'
    cursor.execute(sql)
    count = 0
    f1 = codecs.open(category+"_keywords.txt","a",encoding='utf-8')
    f2 = codecs.open(category+".txt","a",encoding='utf-8')

    # result
    for result in cursor:
        content = result['title']+" "+result['brief']
        keyword = result['keywords'].replace('|',' ')
        contents.append(SentFilter(content)+'\n')
        keywords.append(keyword+'\n')
        if len(keywords) == 100:
            f2.writelines(contents)
            f1.writelines(keywords)
            count += 1
            time_str = datetime.datetime.now().isoformat()
            process = count*100 / total_number *100
            print("{}: processed {:g} % , already write {:g} lines .".format(time_str,process,count*100))
            contents.clear()
            keywords.clear()
    cursor.close()

f1.close()
f2.close()
conn.close()
