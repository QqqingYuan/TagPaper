__author__ = 'PC-LiNing'

import codecs


# input is a dict {'word':weight,...}
def Generate_cloud(file_name,words_dict):
    file = codecs.open(file_name, "a",encoding='utf-8')
    file.write('<!DOCTYPE html>'+'\n')
    file.write('<html><head><title>jQCloud Example</title>'+'\n')
    file.write('<link rel="stylesheet" type="text/css" href="jqcloud.css" />'+'\n')
    file.write('<script type="text/javascript" src="jquery-2.1.1.js"></script>'+'\n')
    file.write('<script type="text/javascript" src="jqcloud-1.0.4.js"></script>'+'\n')
    file.write('<script type="text/javascript">'+'\n')
    file.write(' var word_array = [')
    # write words
    cloud_str = ''
    for word,weight in words_dict.items():
        temp = '{text: "'+word+'", weight: '+str(weight)+'},'
        cloud_str += temp
    file.write(cloud_str+'\n')
    file.write('];'+'\n')
    file.write('$(function() {$("#example").jQCloud(word_array);});</script>'+'\n')
    file.write('</head><body><div id="example" style="width: 550px; height: 350px;"></div></body></html>'+'\n')
    file.close()


words = {'机器学习':9,'LDA':7,'贝叶斯':6,'神经网络':5,'马尔科夫链':15}
Generate_cloud('test.html',words)