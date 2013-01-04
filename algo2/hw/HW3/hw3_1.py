import pandas 
import numpy as np
import math
import copy
import datetime as dt
import csv

knapsackSize=-1
noOfItems=-1
currItem = 0
with open('/Users/ylyakh/class/algo2/hw/HW3/knapsack1.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (knapsackSize == -1):
                        knapsackSize = int(row[0])
                        noOfItems = int(row[1])
                        items = np.zeros(( noOfItems + 1, knapsackSize + 1), dtype=np.int)
                else:
                        currItem = currItem + 1
                        value = int(row[0])
                        weight = int(row[1])
                        for x in range(knapsackSize + 1):
                                if (x < weight):
                                        items[currItem, x] = items[currItem - 1, x]
                                else:
                                        case1 = items[currItem -1, x]
                                        case2 = items[currItem - 1, x - weight] + value
                                        items[currItem, x] = max(case1, case2)

                                
print "====", items[noOfItems, knapsackSize]

