import os
import time
#####################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import yahoo_fin.stock_info as  si
import datetime as dt
from pandas.tseries.offsets import BDay
#######################################

def StockTransaction(paths,configFile):
    print('Transaction Started ')
    print(paths)
    print(configFile)
    print('Starting the stock calculation')
    with open(configFile,'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    stockInInterest = content[0]
    noOfStocks = content[1]
    eMail = content[2]
    marketStartTime=dt.time(8, 30, 0)
    marketEndTime=dt.time(15, 0, 0)
    currentTime = dt.datetime.now().time()
    currentDate = dt.date.today().strftime("%Y-%m-%d")
    print(currentTime)
    print(currentDate)



    print(content)

    while (os.path.isfile(configFile)):
        print(configFile + ' Exits in the path')

        time.sleep(10)
        
        if os.path.isfile(configFile) and (str(dt.date.today().weekday()) in '01234') and ((currentTime >= marketStartTime ) and (currentTime <= marketEndTime)) :
            print('the process keeps running .. The major operation will be done here')
        elif os.path.isfile(configFile) and (str(dt.date.today().weekday()) in '01234') and ((currentTime <= marketStartTime ) or (currentTime >= marketEndTime)) :
            print('Outside the active trading hours in weekdays ... the process will continue to run')

        elif os.path.isfile(configFile) and  (str(dt.date.today().weekday()) not in '01234') :
            print('This is weekend and stock market is closed ... The process will continue to run ')
        elif(not os.path.isfile(configFile)):
            print('The config file deleted and the process will terminate in sometime')
        else:
            print('Unknown reason .. the process will continue to run')

