from datetime import date
import os


def GetStockInfo(paths):
    ''' This process will get all the required informstion from the user which is needed
    to run the proess '''
    ticker = input('Get the ticker name for which you want to run the process : ').upper()
    numberOfStocks = int(input('How many stocks you want to buy for {} : '.format(ticker)))
    emailID = input('Type the email id which will be used in this process : ').lower()

    today = date.today()
    processStartDate = today.strftime("%m%d%Y")
    print('processStartDate =', processStartDate)

    print('The process will run for {} and with {} number of stocks .\nIt '
          'can be tracked with the emailID {} in a daily basis . '.format(ticker,numberOfStocks,emailID))

    configFile = paths['configPath']+'\\'+ticker+'_'+str(numberOfStocks)+'_'+str(processStartDate)

    with open(configFile,'w') as cf:
        cf.write(ticker+'\n')
        cf.write(str(numberOfStocks)+'\n')
        cf.write(emailID+'\n')

    print(configFile + ' Got created !! The process will keep running and to stop remove the configfile')

    return configFile

    #with open(paths['configPath']+'\\'+ticker+str(numberOfStocks)+str(processStartDate))


