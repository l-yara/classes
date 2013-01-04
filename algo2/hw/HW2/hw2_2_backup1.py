import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import datetime as dt
import csv

maxSpacing = 3
nodeSize = 10
step = 100

def calculateDistance(cluster, row):
        dist = 0
        for i in range(0,nodeSize-1):
                if (cluster[i] == "*" or cluster[i] != row[i]):
                        dist = dist + 1
                        if (dist > maxSpacing):
                                return nodeSize
        return dist

def mergeRow2cluster(row, cluster):
        for i in range(0,nodeSize-1):
                if (cluster[i] != row[i]):
                        cluster[i] = "*"
        return cluster
        

board = []
count = 1
with open('/Users/ylyakh/class/algo2/hw/HW2/clustering2-test-4.txt', 'r') as csvfile:
# with open('/Users/ylyakh/class/algo2/hw/HW2/clustering2.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                currRow = row[0:nodeSize]
                if (count % step == 0):
                        print ":", count
#                print currRow
                minimalCluster=None
                minimalDist = nodeSize
                for cluster in board:
                        currDistance = calculateDistance(cluster, currRow)
                        if (currDistance < minimalDist):
                                minimalDist = currDistance
                                minimalCluster = cluster
                if (minimalDist <= maxSpacing):
#                        print "merge", minimalCluster
#                        print " with", currRow
#                        print "on distance ", minimalDist
                        board.remove(minimalCluster)
                        board.append(mergeRow2cluster(currRow, minimalCluster))
                else:
#                        print "appen", currRow, ":", minimalDist
                        board.append(currRow)
                count = count + 1

#edges = sorted(tuples, key=lambda rec: rec[2]) 
#currEdge = edges[0]

print len(board)
print board
