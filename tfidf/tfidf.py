# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

import gensim


def split_text(text):
    return text.strip('\n').strip().split()


class KejsoCorpus(gensim.corpora.TextCorpus):
    def get_texts(self):
        f = open(self.input,encoding='utf8')
        while 1:
            line = f.readline()
            if not line:
                break
            yield split_text(line)


print('generate corpus and dic ...')
corpus = KejsoCorpus('all_reduce_frequency.txt')
dic = corpus.dictionary

print('compute TF-IDF ...')
tfidf = gensim.models.TfidfModel(corpus=corpus,dictionary=dic)

# save dict
print('save dic ...')
dic.save('kejso_words.dict')
# save tf-idf model
print('save TF-IDF model...')
tfidf.save('kejso_tfidf_model')



