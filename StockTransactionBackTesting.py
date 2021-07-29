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
import os
#######################################

def StockTransaction(stockInInterest,noOfStocks):
    print('inside the StockTransaction function Buying and selling in progress')
    print(stockInInterest + str(noOfStocks))
    dateOfInterest =  dt.date.today().strftime("%Y-%m-%d")
    dateOfPrev5thBDay=  (dt.date.today() -BDay(5)).strftime("%Y-%m-%d")
    stock = yf.download(stockInInterest,dateOfPrev5thBDay,interval='5m')['Adj Close']
    stockDf =stock.to_frame(name='Price')
    stockDf['Rolling Mean12'] = stockDf['Price'].rolling(12).mean()
    stockDf['Exp Rolling Mean12'] = stockDf['Price'].ewm(span=12,adjust=False).mean()
    stockDf['Pct Change'] = ((stockDf['Rolling Mean12'] - stockDf['Price'])/stockDf['Price'])*100
    stockDf['Exp Pct Change'] = ((stockDf['Exp Rolling Mean12'] - stockDf['Price']) / stockDf['Price']) * 100

    stockDf['Pct Change'].plot(kind='hist', bins=100)
    plt.show()

    stockDf['Exp Pct Change'].plot(kind='hist', bins=100)
    plt.show()

    print('------------Pct Change Max---------')
    print(stockDf['Pct Change'].max())


    print('------------Exp Pct Change Max---------')
    print(stockDf['Exp Pct Change'].max())


    print('------------Standard Dev---------')
    secondStd = stockDf['Pct Change'].std()*2
    print(secondStd)

    print('------------Exp Standard Dev---------')
    expSecondStd = stockDf['Exp Pct Change'].std() * 2
    print(secondStd)

    todaysSock = stockDf.loc[dateOfInterest]
    todaysSock['Sell Price'] = todaysSock['Price'].shift(-1)

    todaysSock[['Price','Exp Rolling Mean12','Sell Price']].plot()



    plt.show()
    print(todaysSock.tail())

    print('------------Stocks Bought---------')


    stocksBought = todaysSock[ todaysSock['Pct Change'] > expSecondStd ]

    print(stocksBought)


    print((stocksBought['Sell Price']-stocksBought['Price']))
    print((stocksBought['Sell Price'] - stocksBought['Price']).sum())
    #
    #
    # todaysSock1 = todaysSock['Pct Change'] > secondStd
    # print(todaysSock1)
    # todaysSock2 = todaysSock
    #
    # # print(stockDf.loc[dateOfInterest]['Pct Change'] > secondStd)
    # #
    # # df = stockDf.loc[dateOfInterest]['Pct Change'] > secondStd
    # #
    # # stockDf[[df]]




    # print(type(stockDf))
    # print('Columns -->'+ stockDf.columns)
    # #stock['Rolling Mean12'] = stock['Adj Close']
    # print('------------Count---------')
    # print(stockDf.count())
    # print('------------Head---------')
    # print(stockDf.head())
    #
    # print('------------Tail---------')
    # print(stockDf.tail())
    #
    # print('------------IDX Max---------')
    # print(stockDf.idxmax())
    #
    # print(dateOfInterest)
    # print(dateOfPrev5thBDay)

StockTransaction('NIO',30)


