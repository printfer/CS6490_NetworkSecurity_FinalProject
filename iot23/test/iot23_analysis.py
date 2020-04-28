#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances

botnet_list = []
with open("botnet_name_list.txt") as file:
    for line in file: 
        botnet_list.append(line[:-1]) #storing everything in memory!

other_list = []
with open("other_name_list.txt") as file:
    for line in file: 
        other_list.append(line[:-1]) #storing everything in memory!

# df = pd.read_csv("./result.csv", header=None)
df = pd.read_csv("./result.csv", delim_whitespace=True, header=None)
print(df.head(10))

botnet_index_list = []
other_index_list = []
#print(botnet_list)
count = 0
for i in df[0]:
    # print(i)
    i = str(i)
    if i in botnet_list:
        #print("bot")
        botnet_index_list.append(count)

    elif i in other_list:
        #print("other")
        other_index_list.append(count)

    count = count + 1

# print(df[0])
#print("test")
#print(df.loc[10, 1:])

fig, ax = plt.subplots(1, 1, figsize = (8, 10))

title = "IoT 23"

plt.title(title, fontsize=18)
ttl = ax.title
ttl.set_position([0.5, 1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis("off")

# print("test1")
# sns.heatmap(df.loc[10, 1:])
# plt.show()


print("fig1")
# dist = euclidean_distances(df.loc[10, 1:], df.loc[10, 1:], squared=True)
# dist = euclidean_distances(df.loc[['192168100103', '92214229122' ], 1:], df.loc[['192168100103', '92214229122' ], 1:], squared=True)
# dist = euclidean_distances(df.loc[[192168100103, 92214229122 ], 1:], df.loc[[192168100103, 92214229122 ], 1:], squared=True)
# dist = euclidean_distances(df.loc[list(range(0, 500)), 1:], df.loc[list(range(0, 500)), 1:], squared=True)
dist = euclidean_distances(df.loc[botnet_index_list[0:10], 1:], df.loc[other_index_list[0:100], 1:], squared=True)
sns.heatmap(dist)

plt.savefig('iot23_result.png')


print("fig2")
dist = euclidean_distances(df.loc[botnet_index_list[0:100], 1:], df.loc[other_index_list[0:100], 1:], squared=True)
sns.heatmap(dist)

plt.savefig('iot23_result_100.png')

