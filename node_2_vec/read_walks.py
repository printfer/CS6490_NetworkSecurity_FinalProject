from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

from node2vec import Node2Vec
import pandas as pd
import numpy as np

import networkx as nx
from scipy.special import softmax
import matplotlib.pyplot as plt
from numba import jitclass
from numba import int32, float32, boolean

import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import euclidean_distances


dsn = pd.read_csv('data/scenario_11.csv')

dsn['Label'] = dsn['Label'].str.lower()

dsn.loc[dsn['Label'].str.contains('botnet'), 'Label'] = 'botnet'
dsn.loc[dsn['Label'].str.contains('background'), 'Label'] = 'background'
dsn.loc[dsn['Label'].str.contains('from-normal'), 'Label'] = 'from-normal'
dsn.loc[dsn['Label'].str.contains('to-normal'), 'Label'] = 'to-normal'

dsn['Label'].unique()

unique_nodes = set(dsn['SrcAddr'].unique()).union(set(dsn['DstAddr'].unique()))

botnets = dsn.loc[dsn['Label'].str.contains('botnet')]
tonormal = dsn.loc[dsn['Label'].str.contains('to-normal')]
fromnormal = dsn.loc[dsn['Label'].str.contains('from-normal')]
background = dsn.loc[dsn['Label'].str.contains('background')]

normalsample = np.concatenate((fromnormal['SrcAddr'].unique(), tonormal['DstAddr'].unique()))
botnetsample = botnets['SrcAddr'].unique()
backgroundsample = np.concatenate((background.sample(n=4)['SrcAddr'].unique(), background.sample(n=3)['DstAddr'].unique()))

print(normalsample)
print(botnetsample)


# For Scenario 11
modelwv = KeyedVectors.load('mywordvecs.kvmodel')

botembeddings = np.array([modelwv[x] for x in botnetsample])
backembeddings = np.array([modelwv[x] for x in backgroundsample])
normalembeddings = np.array([modelwv[x] for x in normalsample])


combinedembeddings = np.concatenate((botembeddings, normalembeddings))
combinedsample = np.concatenate((botnetsample, normalsample))

euclid = euclidean_distances(combinedembeddings, combinedembeddings, squared=True)
ax = sns.heatmap(np.array(euclid))
plt.title('Bad vs. Normal IPS\n(node2vec, euclidean distance)')
plt.yticks(range(len(combinedsample)), labels=combinedsample, rotation=0)
plt.xticks(range(len(combinedsample)), labels=combinedsample, rotation=90)
plt.tight_layout()
plt.savefig("Bad_Normal_Euclidean.png")
plt.show()

cosine = cosine_similarity(combinedembeddings, combinedembeddings)
ax = sns.heatmap(np.array(cosine))
plt.title('Bad vs. Normal IPS\n(node2vec, cosine similarity)')
plt.yticks(range(len(combinedsample)), labels=combinedsample , rotation=0)
plt.xticks(range(len(combinedsample)), labels=combinedsample, rotation=90)
plt.tight_layout()
plt.savefig("Bad_Normal_Cosine.png")
plt.show()


combinedembeddings = np.concatenate((botembeddings, backembeddings))
combinedsample = np.concatenate((botnetsample, backgroundsample))

euclid = euclidean_distances(combinedembeddings, combinedembeddings, squared=True)
ax = sns.heatmap(np.array(euclid))
plt.title('Bad vs. Random Background IPS\n(node2vec, euclidean distance)')
plt.yticks(range(len(combinedsample)), labels=combinedsample, rotation=0)
plt.xticks(range(len(combinedsample)), labels=combinedsample, rotation=90)
plt.tight_layout()
plt.savefig("Bad_Random_Euclidean.png")
plt.show()

cosine = cosine_similarity(combinedembeddings, combinedembeddings)
ax = sns.heatmap(np.array(cosine))
plt.title('Bad vs. Random Background IPS\n(node2vec, cosine similarity)')
plt.yticks(range(len(combinedsample)), labels=combinedsample , rotation=0)
plt.xticks(range(len(combinedsample)), labels=combinedsample, rotation=90)
plt.tight_layout()
plt.savefig("Bad_Random_Cosine.png")
plt.show()