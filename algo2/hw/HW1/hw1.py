import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import datetime as dt
import csv

tuples = []
with open('/Users/ylyakh/class/algo2/hw/HW1/jobs.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
#                print row[0]
                weight = int(row[0])
                length = int(row[1])
                tuples.append((weight, length, (weight-length), (float(weight)/length)))
# print tuples
sorted = sorted(tuples, key=lambda rec: -rec[2] * 1000 - rec[0]) 
# sorted = sorted(tuples, key=lambda rec: -rec[3]) 
# print sorted
c = 0
w = 0
for job in sorted:
        c = c + job[1]
        w = w + c * job[0]
        print job , " ", c, ":", w

print c, "=====", w
