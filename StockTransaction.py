import os
import time
import time as tm
def StockTransaction(paths,configFile):
    print('Transaction Started ')
    print(paths)
    print(configFile)

    while (os.path.isfile(configFile)):
        print(configFile + ' Exits in the path')
        time.sleep(5)
        if os.path.isfile(configFile):
            print('the process keeps running')
        else:
            print(configFile + ' Removed .. the process will terminate in sometime')

