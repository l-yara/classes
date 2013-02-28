import pandas 
import numpy as np
import math
import copy
import datetime as dt
import csv

m=-1
n=-1
main = []
inf = 10**12 - 1
# with open('/Users/ylyakh/class/algo2/hw/HW4/large.txt', 'r') as csvfile:
with open('/Users/ylyakh/class/algo2/hw/HW4/g3.txt', 'r') as csvfile:
# with open('/Users/ylyakh/class/algo2/hw/HW4/cycles2.txt', 'r') as csvfile:
# with open('/Users/ylyakh/class/algo2/hw/HW4/sp-6.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (n == -1): 
                        n = int(row[0])
                        m = int(row[1])
                        # items = np.zeros(( noOfItems + 1, knapsackSize + 1),
                        # dtype=np.int)
                        main = np.ones((n, n), dtype = np.int) * inf;
                        for i in range(n):
                                main[i, i] = 0
                else:
                        src = int(row[0])-1
                        dest = int(row[1])-1
                        main[src, dest] = int(row[2])

# print main

for k in range(n):
        print "-------------------", k
        prev_step = main
        main = np.zeros((n, n), dtype = np.int)
        for i in range(n):
                for j in range(n):
                        case_1 = prev_step[i, j]
                        case_2 = prev_step[i, k] + prev_step[k, j]
                        main[i, j] = min(case_1, case_2)
                        if (i == j and main[i, j] < 0):
                                print "ooops", i, j, k, main[i, j]
                                SystemExit(0)
        # print main
                        

                                
# print main                      
print "====", np.amin(main)

