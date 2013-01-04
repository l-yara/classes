import pandas 
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import qstkutil.qsdateutil as du
import datetime as dt
import qstkutil.DataAccess as da
import qstkutil.tsutil as tsu
import qstkstudy.EventProfiler as ep

# Get the data from the data store
storename = "Yahoo" # get data from our daily prices source
# Available field names: open, close, high, low, close, actual_close, volume
closefield = "actual_close"
volumefield = "volume"
# window = 10
eventThreachold = 7.0

def findEvents(symbols, startday,endday, marketSymbol,verbose=False):

	# Reading the Data for the list of Symbols.	
	timeofday=dt.timedelta(hours=16)
	timestamps = du.getNYSEdays(startday,endday,timeofday)
	dataobj = da.DataAccess('Yahoo')
	if verbose:
            print __name__ + " reading data"
	# Reading the Data
	close = dataobj.get_data(timestamps, symbols, closefield)
	
	# Completing the Data - Removing the NaN values from the Matrix
#	close = (close.fillna(method='ffill')).fillna(method='backfill')

	
	# Calculating Daily Returns for the Market
#!!!	tsu.returnize0(close.values)
#	SPYValues=close[marketSymbol]

	# Calculating the Returns of the Stock Relative to the Market 
	# So if a Stock went up 5% and the Market rised 3%. The the return relative to market is 2% 
#	mktneutDM = close - close[marketSymbol]
	np_eventmat = copy.deepcopy(close)
	for sym in symbols:
		for time in timestamps:
			np_eventmat[sym][time]=np.NAN

	if verbose:
            print __name__ + " finding events"

	# Generating the Event Matrix
	# Event described is : Market falls more than 3% plus the stock falls 5% more than the Market
	# Suppose : The market fell 3%, then the stock should fall more than 8% to mark the event.
	# And if the market falls 5%, then the stock should fall more than 10% to mark the event.
        output = open("hw4.csv", "w")

        totalDays = len(close[marketSymbol])
        for i in range(1, totalDays):
                for symbol in symbols:
                        if close[symbol][timestamps[i-1]] >= eventThreachold and close[symbol][timestamps[i]] < eventThreachold :
                                moment = timestamps[i]
                                output.write('%(year)04d,%(month)02d,%(day)02d,%(symbol)s,Buy, 100 \n' % {"year":moment.year, "month":moment.month, "day":moment.day, "symbol":symbol })
                                sellMomentIndex = min(i + 5, totalDays-1)
#                                print "i:", i, ", totalDays: ", totalDays, "===", sellMomentIndex
                                moment = timestamps[sellMomentIndex]
                                output.write('%(year)04d,%(month)02d,%(day)02d,%(symbol)s,Sell,100 \n' % {"year":moment.year, "month":moment.month, "day":moment.day, "symbol":symbol })
                                np_eventmat[symbol][i] = 1.0  #overwriting by the bit, marking the event

        output.close()
	return np_eventmat



#################################################
################ MAIN CODE ######################
#################################################


# symbols = np.loadtxt('SP500port.csv',dtype='S10',comments='#', skiprows=1)
# You might get a message about some files being missing, don't worry about it.

dataobj = da.DataAccess('Yahoo')
symbols = dataobj.get_symbols_from_list("sp5002012")
symbols.append('SPY')

#symbols =['BFRE','ATCS','RSERF','GDNEF','LAST','ATTUF','JBFCF','CYVA','SPF','XPO','EHECF','TEMO','AOLS','CSNT','REMI','GLRP','AIFLY','BEE','DJRT','CHSTF','AICAF']
# startday = dt.datetime(2012,1,1)
# endday = dt.datetime(2012,12,31)
startday = dt.datetime(2008,1,1)
endday = dt.datetime(2009,12,31)

eventMatrix = findEvents(symbols,startday,endday,marketSymbol='SPY',verbose=True)

eventProfiler = ep.EventProfiler(eventMatrix,startday,endday,lookback_days=20,lookforward_days=20,verbose=True)

eventProfiler.study(filename="MyEventStudyHW.pdf",plotErrorBars=True,plotMarketNeutral=True,plotEvents=False,marketSymbol='SPY')


