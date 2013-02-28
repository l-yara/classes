import itertools
import pandas 
import numpy as np
import math
import random
import copy
import datetime as dt
import csv

n=-1
main = []
with open('/Users/ylyakh/class/algo2/hw/HW6/2sat2.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
                if (n == -1): 
                        n = int(row[0])
                else:
                        x = int(row[0])
                        y = int(row[1])
                        main.append((x, y))

attempts=int(math.ceil(math.log(n, 2)))
versions = 2*(n**2)

print versions, attempts

for m in range(attempts):
        values = np.random.randint(0, 2, n+1)
        print "------------", m, "of", attempts
        # print "-------------------", values
        version = 0
        while version < versions:
                if (version%1000 == 0):
                        print "----", version, "of", versions, ":", dt.datetime.now()
                # print "----", version, "of", versions, ":", values
                passed = 1
                for single in main:
                        var1 = single[0]
                        var2 = single[1]
                        if (var1 > 0 and values[var1]):
                                continue
                        if (var1 < 0 and (not values[-var1])):
                                continue
                        if (var2 > 0 and values[var2]):
                                continue
                        if (var2 < 0 and (not values[-var2])):
                                continue
                        passed = 0
                        swapIndex = 0
                        if (random.randint(0, 1)):
                                swapIndex = int(math.fabs(var1))
                        else:
                                swapIndex = int(math.fabs(var2))
                        # print "OOOOOPS!", single, swapIndex
                        values[swapIndex] = not values[swapIndex]
                        break
                if (passed):
                        print "WOOHOOO!"
                        System.exit(0)
                version = version + 1
if (not passed):
        print "TOUGH LUCK!"
