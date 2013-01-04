# python imports
import cPickle
import sys
import numpy as np
# from pandas import DataMatrix
import datetime as dt
import random

# qstk imports
import qstkutil.DataAccess as da
import qstkutil.qsdateutil as du


print "Running the market simulation tool with "+sys.argv[1] +" money, to "+sys.argv[2] 
orders = np.loadtxt(sys.argv[2],delimiter=',',dtype='i4, i1, i, S4, S4, i',comments='#',skiprows=0)

print "!!!!!!", orders.dtype
# orders.dtype = [('f0', 'i4'), ('f1', 'i4'), ('f2', 'i4'), ('f3', 'S4'), ('f4', 'S4'), ('f5', 'i4')]
#orders.dtype = np.dtype({'names':['year' })

startday = dt.date(orders[0][0], orders[0][1], orders[0][2])
endday = dt.date(orders[-1][0], orders[-1][1], orders[-1][2])

print "printing data between", startday, "and", endday
timeofday=dt.timedelta(hours=16)
timestamps = du.getNYSEdays(startday,endday,timeofday)

workingSymbols = set()
orderAmount = orders.shape[0]
for i in range(0, orderAmount):
    workingSymbols.add(orders[i][3])

# print "timestamps", timestamps

dataobj = da.DataAccess('Yahoo')
# Reading the Data
close = dataobj.get_data(timestamps, workingSymbols, "actual_close")

cache=float(sys.argv[1])
portfolio={}
nextOrder = 0
output = open(sys.argv[3], "w")
for moment in timestamps:
    todayOrders = orders[(orders['f2'] == moment.day) & (orders['f1'] == moment.month) & (orders['f0'] == moment.year) ]
    for singleOrder in todayOrders:
        symbol = singleOrder[3]
        amount = singleOrder[5]
        if singleOrder[4] == 'Sell':
            amount = -amount
        if symbol in portfolio:
            portfolio[symbol] = portfolio[symbol] + amount
        else:
            portfolio[symbol] = amount
        price = close[symbol][moment]
        cache = cache - price * amount
        print symbol, price, amount, price * amount, cache
        nextOrder = nextOrder + 1

    currValue=cache
    for symbol in portfolio.viewkeys():
        currValue = currValue + portfolio[symbol] * close[symbol][moment]
    print moment.date(), currValue, portfolio, nextOrder, "!!!", cache
    output.write('%(year)04d,%(month)02d,%(day)02d,%(value)d \n' % {"year":moment.year, "month":moment.month, "day":moment.day, "value":currValue })
#    output.write(str(currValue) + "\n")

        
output.close
print "target: 1133860"


