import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import datetime as dt
import csv

maxSpacing = 2
nodeSize = 24
step = 100

allRows = []

def inDistance(cluster, row):
#        print "in Distance: ", cluster, " vs ", row
        clusterHash = cluster['hash']
        distHash = 0
        for i in range(0,nodeSize):
                if (clusterHash[i] != "*" and clusterHash[i] != row[i]):
                        distHash = distHash + 1
                        if (distHash > maxSpacing):
 #                               print "hash check: failed : ", distHash
                                return 0
        # hash check OK, now check every row
        for clusterRowId in cluster['rows']:
                # check 
                dist=0
                clusterRow = allRows[clusterRowId]
#                print "checking ", row, " vs ", clusterRow
                for i in range(0,nodeSize):
                        if (clusterRow[i] != row[i]):
                                dist = dist + 1
                                if (dist > maxSpacing):
#                                        print "== per-row break:", clusterRow, " of ", clusterRowId
                                        break
                if (dist <= maxSpacing):
                        return 1
#        print "per-row failed: ", cluster['rows']
        return 0

def mergeRow2clusters(count, clusters):
        mergedHash = map( lambda char: char, allRows[count])
        rowIds = [count]
#        print "merge:", mergedHash
        for cluster in clusters:
                for i in range(0,nodeSize):
                        if (cluster['hash'][i] != mergedHash[i]):
                                mergedHash[i] = "*"
                rowIds = rowIds + cluster['rows']
        return {'hash': mergedHash, 'rows':sorted(rowIds)}

board = []

# with open('/Users/ylyakh/class/algo2/hw/HW2/clustering2-test-4.txt', 'r') as csvfile:
with open('/Users/ylyakh/class/algo2/hw/HW2/clustering2.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                currRow = row[0:nodeSize]
                allRows.append(currRow)
#                print currRow
                count = len(allRows) - 1
                if (count % step == 0):
                        print count, ":", currRow

                mergeClusters = []
                for cluster in board:
                        currDistance = inDistance(cluster, currRow)
                        if (currDistance):
                                mergeClusters.append(cluster)
                if (mergeClusters != []):
#                        print " with", currRow
#                        print "on distance ", minimalDist
                        
                        for toMerge in mergeClusters:
                                board.remove(toMerge)
                        newCluster= mergeRow2clusters(count,  mergeClusters)
#                        print "merge", mergeClusters, " to ", newCluster 
                        board.append(newCluster)
                else:
                        newCluster = {'hash': currRow, 'rows':[count]}
#                        print "appen", currRow, ":", newCluster
                        board.append(newCluster)

#edges = sorted(tuples, key=lambda rec: rec[2]) 
#currEdge = edges[0]

print "=====" , len(board)
#for cluster in board:
#        print cluster
