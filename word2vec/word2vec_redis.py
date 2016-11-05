# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

from gensim.models.word2vec import Word2Vec
import numpy as np
import redis
import datetime


# redis
r = redis.StrictRedis(host='10.2.1.4', port=6379, db=0)

model = Word2Vec.load_word2vec_format('word2vec/wikivectors.bin',binary=True)

# word_embedding_size = 200

wordVocab = [ k for (k,v) in model.vocab.items()]

vocab_size = len(wordVocab)

print("model vocab size: "+str(vocab_size))

for i in range(0,vocab_size):
    if i % 1000 == 0:
        time_str = datetime.datetime.now().isoformat()
        process = i / vocab_size * 100
        print("{}: processed {:g} % , already have {:g} words.".format(time_str,process,i))
        r.save()
    word = wordVocab[i]
    vec = model[word]
    r.set(word,vec.tostring())

r.save()

print("Total words: {:g}".format(vocab_size))
print("Finished!")

