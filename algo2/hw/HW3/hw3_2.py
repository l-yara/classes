import pandas 
import numpy as np
import math
import copy
import datetime as dt
import csv

knapsackSize=-1
noOfItems=-1
currItem = 0
with open('/Users/ylyakh/class/algo2/hw/HW3/knapsack2.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (knapsackSize == -1):
                        knapsackSize = int(row[0])
                        noOfItems = int(row[1])
                        items = np.zeros(knapsackSize + 1, dtype=np.int)
                else:
                        currItem = currItem + 1
                        value = int(row[0])
                        weight = int(row[1])
                        newItems = np.zeros(knapsackSize + 1, dtype=np.int)
                        for x in range(weight):
                                newItems[x] = items[x]
                        for x in range(weight, knapsackSize + 1):
                                case1 = items[x]
                                case2 = items[x - weight] + value
                                newItems[x] = max(case1, case2)
                        items = newItems
                                
print "====", items[knapsackSize]
#print items[...]
#for row in items[...]:
#        print row
# print items

