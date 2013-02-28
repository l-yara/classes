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
# with open('/Users/ylyakh/class/algo2/hw/HW4/cycles2.txt', 'r') as csvfile:
with open('/Users/ylyakh/class/algo2/hw/HW4/sp-7.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (n == -1): 
                        n = int(row[0])
                        m = int(row[1])
                        # items = np.zeros(( noOfItems + 1, knapsackSize + 1),
                        # dtype=np.int)
                        main = np.zeros((n, n), dtype = np.int);
                else:
                        src = int(row[0])-1
                        dest = int(row[1])-1
                        weight = int(row[2])
                        main[src, dest] = 1

print main

for k in range(n):
        print "-------------------", k
        prev_step = main
        main = np.zeros((n, n), dtype = np.int)
        for i in range(n):
                for j in range(n):
                        main[i, j] = prev_step[i, j] + prev_step[i, k]* prev_step[k, j] 
                                
        print main
                        

                                
# print main                      
print "====", np.amin(main)

