from node2vec import Node2Vec
import pandas as pd
import numpy as np

import networkx as nx
from scipy.special import softmax
import matplotlib.pyplot as plt
from numba import jitclass
from numba import int32, float32, boolean

dsn = pd.read_csv('data/scenario_11.csv')

dsn['Label'].unique()

unique_nodes = set(dsn['SrcAddr'].unique()).union(set(dsn['DstAddr'].unique()))

unique_edges = dsn[['SrcAddr', 'DstAddr']].drop_duplicates()
unique_edges = unique_edges.to_records(index=False)
unique_edges = list(unique_edges)

G = nx.Graph()
G.add_nodes_from(unique_nodes)
G.add_edges_from(unique_edges)

# Generate walks
node2vec = Node2Vec(G, dimensions=10, walk_length=10, num_walks=10)

model = node2vec.fit(window=10, min_count=1)

model.wv.save('mywordvecs10.kvmodel')


