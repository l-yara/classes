import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import datetime as dt
import csv

nodes = 50
k = 4

tuples = []
with open('/Users/ylyakh/class/algo2/hw/HW2/clustering1_test.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
#                print row[0]
                v1 = int(row[0])
                v2 = int(row[1])
                weight = int(row[2])
                tuples.append((v1, v2, weight))
# print tuples
edges = sorted(tuples, key=lambda rec: rec[2]) 
clusters = map(lambda i: {i+1}, range(nodes))
# sorted = sorted(tuples, key=lambda rec: -rec[3]) 

#print edges
currEdge = edges[0]

while (edges != [] and len(clusters)>=k):
        currEdge = edges[0]
        edges.remove(currEdge)
#        print currEdge, " left : ", edges
        c1 = filter(lambda cluster: currEdge[0] in cluster, clusters)[0]
        c2 = filter(lambda cluster: currEdge[1] in cluster, clusters)[0]
#        print c1, " === ", c2
        if (c1 != c2):
                clusters.append(c1 | c2)
                clusters.remove(c1)
                clusters.remove(c2)



print edges[0:10]
print clusters
print currEdge
