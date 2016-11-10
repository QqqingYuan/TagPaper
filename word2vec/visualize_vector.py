# -*- coding: utf-8 -*-

__author__ = 'PC-LiNing'

from sklearn.manifold import TSNE
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Droid Sans Fallback']
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import load_data


def plot_with_labels(low_dim_embs, labels, filename='tsne.png'):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  #in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i,:]
        plt.scatter(x, y)
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')

    plt.savefig(filename)


words,embeddings = load_data.getEmbedding_Label()
tsne = TSNE(perplexity=30,n_components=2,init='pca',n_iter=5000)
plot_only = 500

low_dim_embs = tsne.fit_transform(embeddings)
plot_with_labels(low_dim_embs,words)


