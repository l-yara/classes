import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import datetime as dt
import csv

edges=[]
with open('/Users/ylyakh/class/algo2/hw/HW1/edges.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                v1 = int(row[0])
                v2 = int(row[1])
                cost = int(row[2])
                edges.append((v1, v2, cost))
print edges
sorted = sorted(edges, key=lambda rec: rec[2])
print sorted

init = sorted[0]
sorted.remove(init)
X= set([init[0], init[1]])
total = init[2]
i = 0
while (sorted != []):
        print len(sorted)
        first = sorted[i]
#        print i, ":", first, ";", X, "===", sorted
        if (first[0] in X and first[1] in X):
#                print "just remove"
                sorted.remove(first)
                i = 0
                continue
        elif (first[0] in X or first[1] in X):
#                print "remove and include"
                X.add(first[0])
                X.add(first[1])
                total = total + first[2]
                sorted.remove(first)
                i = 0
                continue
        else:
                print "neeext"
                i = i + 1


print total
