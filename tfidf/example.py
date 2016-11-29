__author__ = 'PC-LiNing'

import gensim

# load dic
dictionary = gensim.corpora.Dictionary.load('kejso_words.dict')
# load model
tfidf = gensim.models.TfidfModel.load('kejso_tfidf_model')

text = "高速切削 淬硬模具钢 切屑形态 的 试验研究 通过 刀具 对 淬硬模具钢 进行 了 高速 切削试验 对 不同 切削速度 下 的 切屑形态 进行 了 宏观 和 微观分析"
text = text.split()
bows = dictionary.doc2bow(text)
result = tfidf[bows]
print(result)
print('#######')
for word in result:
    print(dictionary[word[0]]+" "+str(word[1]))
