import GetStockInfo
import Manual
import Promise
import StockTransaction

paths={'configPath': r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\config',
       'logPath': r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\log',
       'mailPath': r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\mail',
       'statsPath': r'C:\Users\abhis\OneDrive\Documents\Abhishek\Stock\stats'}



def main():
    try:

        Promise.Promise(paths)
        Manual.Manual(paths)
        configFile = GetStockInfo.GetStockInfo(paths)
        StockTransaction.StockTransaction(paths,configFile)

        print(configFile)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()