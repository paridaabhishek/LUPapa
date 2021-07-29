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

def StockTransaction(stockInInterest,noOfStocks,processStartDate):



    print('inside the StockTransaction function Buying and selling in progress')
    print(stockInInterest + str(noOfStocks))
    dateOfInterest =  dt.date.today().strftime("%Y-%m-%d")
    dateOfPrev5thBDay=  (dt.date.today() -BDay(5)).strftime("%Y-%m-%d")
    stock = yf.download(stockInInterest,dateOfPrev5thBDay,interval='5m')['Adj Close']
    stockDf =stock.to_frame(name='Price')

##################### File path declaration ###################################################################################
    transactionFilePath = r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\transactions'+'\\'
    buyTempFile = stockInInterest+'_'+str(noOfStocks)+'_'+str(processStartDate)+'_'+str(dateOfInterest)+'_Buy.csv'
    sellTempFile =stockInInterest+'_'+str(noOfStocks)+'_'+str(processStartDate)+'_'+str(dateOfInterest)+'_Sell.csv'
    transMasterFile =stockInInterest+'_'+str(noOfStocks)+'_'+str(processStartDate)+'_MasterTrans.csv'

    print(transactionFilePath)
    print(buyTempFile)
    print(sellTempFile)
    print(transMasterFile)





###################Parameter calculation########################################################################################
    stockDf['Rolling Mean12'] = stockDf['Price'].rolling(12).mean()
    stockDf['Exp Rolling Mean12'] = stockDf['Price'].ewm(span=12,adjust=False).mean()
    stockDf['Pct Change'] = ((stockDf['Rolling Mean12'] - stockDf['Price'])/stockDf['Price'])*100
    stockDf['Exp Pct Change'] = ((stockDf['Exp Rolling Mean12'] - stockDf['Price']) / stockDf['Price']) * 100




    # stockDf['Pct Change'].plot(kind='hist', bins=100)
    # plt.show()

    # stockDf['Exp Pct Change'].plot(kind='hist', bins=100)
    # plt.show()

    print('------------Pct Change Max---------')
    print(stockDf['Pct Change'].max())


    print('------------Exp Pct Change Max---------')
    print(stockDf['Exp Pct Change'].max())


    print('------------Standard Dev---------')
    secondStd = stockDf['Pct Change'].std()*2
    print(secondStd)

    print('------------Exp Standard Dev---------')
    expSecondStd = stockDf['Exp Pct Change'].std() * 2
    print(expSecondStd)



    todaysSock = stockDf.loc[dateOfInterest]
    #todaysSock = stockDf.loc['07-28-2021']
    todaysSock['No of stocks'] = noOfStocks

    print('------------Todays Stock---------')
    print(todaysSock)

    print('------------Todays Stock max---------')



    latestStockPrice = todaysSock.iloc[-1:]
    print(latestStockPrice)

    print(latestStockPrice['Exp Pct Change'] > -1)

    value = latestStockPrice['Exp Pct Change'].values[0]

    print('------------Value---------')
    print(value)

    print(type(latestStockPrice))
    #
    # if (latestStockPrice.ge(2)):
    #     print('GE-1')

    if os.path.isfile(transactionFilePath+buyTempFile):
        sellStock = pd.read_csv(transactionFilePath+buyTempFile, index_col='Datetime')
        sellStock['Sell Price'] = latestStockPrice['Price'].values[0]
        print('------------Sell Stock ---------')
        print(sellStock)
        sellStock.to_csv(transactionFilePath+sellTempFile)
        if os.path.isfile(transactionFilePath+transMasterFile):
            sellStock.to_csv(transactionFilePath + transMasterFile, mode='a', header=False)
        else:
            sellStock.to_csv(transactionFilePath + transMasterFile)
        os.remove(transactionFilePath+buyTempFile)
        os.remove(transactionFilePath+sellTempFile)





    #
    #

    if (latestStockPrice['Exp Pct Change'].values[0] > -1 ):  #expSecondStd
        print('Buying the stock') #The actual buying code will be here
        latestStockPrice.to_csv(transactionFilePath+buyTempFile)
        # with open(r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\transactions\NIO_30_20210728.txt','w') as f:
        #     f.write(str(latestStockPrice.to_frame()))

    else:
        print('No Action')



    # todaysSock['Sell Price'] = todaysSock['Price'].shift(-1)
    #
    # todaysSock[['Price','Exp Rolling Mean12','Sell Price']].plot()
    #
    #
    #
    # plt.show()
    # print(todaysSock.tail())
    #
    # print('------------Stocks Bought---------')
    #
    #
    # stocksBought = todaysSock[ todaysSock['Pct Change'] > expSecondStd ]
    #
    # print(stocksBought)
    #
    #
    # print((stocksBought['Sell Price']-stocksBought['Price']))
    # print((stocksBought['Sell Price'] - stocksBought['Price']).sum())
    # #
    # #
    # # todaysSock1 = todaysSock['Pct Change'] > secondStd
    # # print(todaysSock1)
    # # todaysSock2 = todaysSock
    # #
    # # # print(stockDf.loc[dateOfInterest]['Pct Change'] > secondStd)
    # # #
    # # # df = stockDf.loc[dateOfInterest]['Pct Change'] > secondStd
    # # #
    # # # stockDf[[df]]
    #
    #
    #
    #
    # # print(type(stockDf))
    # # print('Columns -->'+ stockDf.columns)
    # # #stock['Rolling Mean12'] = stock['Adj Close']
    # # print('------------Count---------')
    # # print(stockDf.count())
    # # print('------------Head---------')
    # # print(stockDf.head())
    # #
    # # print('------------Tail---------')
    # # print(stockDf.tail())
    # #
    # # print('------------IDX Max---------')
    # # print(stockDf.idxmax())
    # #
    # # print(dateOfInterest)
    # # print(dateOfPrev5thBDay)

StockTransaction('NKLA',30,'2021-07-26')


