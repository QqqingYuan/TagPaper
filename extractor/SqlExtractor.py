# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import pymysql
import Util
import datetime

config = {
    'host':'10.2.16.252',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'kejso_solrdata',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor
}

conn = pymysql.connect(**config)

contents = []
total_number = 1000
with conn.cursor() as cursor:
    sql = 'select title_cn,abstract_cn from paper_wanfang limit 10000000,1000'
    cursor.execute(sql)
    count = 0
    f = open("paper.txt","w+")

    # result
    for result in cursor:
        content = result['title_cn']+" "+result['abstract_cn']
        contents.append(Util.SegSentence(content))
        if len(contents) == 100:
            f.writelines(contents)
            count += 1
            time_str = datetime.datetime.now().isoformat()
            process = count*100 / total_number *100
            print("{}: processed {:g} % , already write {:g} lines .".format(time_str,process,count*100))
            contents.clear()
    cursor.close()

f.close()
conn.close()
