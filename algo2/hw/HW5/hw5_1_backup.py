import itertools
import pandas 
import numpy as np
import math
import copy
import datetime as dt
import csv

def index_of(s_set, exclude):
        ret = 0
        for i in s_set:
                if (i != exclude) :
                        ret = ret + 2**i
        return ret

def dist(src, dest):
        dx = cities[src][0]-cities[dest][0]
        dy = cities[src][1]-cities[dest][1]
        # print cities[src][0], cities[dest][0], "!!!!", math.sqrt(dx * dx + dy * dy) 
        return math.sqrt(dx * dx + dy * dy)


s=-1
n=-1
main = []
cities = []
inf = 10**6 - 1
with open('/Users/ylyakh/class/algo2/hw/HW5/tsp5.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (n == -1): 
                        n = int(row[0])
                        s = 2**(n)
                        main = np.ones((s, n), dtype = np.int) * inf;
                        for i in range(n):
                                main[0, i] = 0
                else:
                        x = float(row[0])
                        y = float(row[1])
                        cities.append((x, y))

print cities

for m in range(1, n):
        S = map(lambda tp: (0,) + tp, list(itertools.combinations(range(1, n),m))) 
        print "-------------------", m, S
        for s_set in S:
                # S - set:
                s_index = index_of(s_set, -1) - 1
                # print s_set, s_index
                for j in s_set:
                        if (j != 0):
                                # index for S-{j}:
                                s_j_index = index_of(s_set, j) - 1
                                # print "=", j, s_j_index
                                curr_min = main[s_j_index, 0] + dist(0, j)
                                for k in s_set:
                                        if (k != j):
                                                curr_min = min(curr_min, main[s_j_index, k] + dist(k, j))
                                               # print "===" , k, curr_min
                                main[s_index, j] = curr_min
print main
ret = inf
s = 2**n - 2
for j in range(1, n):
        ret = min(ret, main[s, j] + dist(j, 0))

print "---", ret, s
        

                        
        
        # prev_step = main
        # main = np.zeros((n, n), dtype = np.int)
        # for i in range(n):
        #         for j in range(n):
        #                 case_1 = prev_step[i, j]
        #                 case_2 = prev_step[i, k] + prev_step[k, j]
        #                 main[i, j] = min(case_1, case_2)
        #                 if (i == j and main[i, j] < 0):
        #                         print "ooops", i, j, k, main[i, j]
                                # SystemExit(0)
        # print main
                        
                                
# print "====", cities, main  
# first five - 8387, first six - 8609
