import rqdatac
import os
import pickle
import tushare as ts
import time
import sys
import datetime
rqdatac.init()
current_time = datetime.datetime.now().strftime("%Y%m%d")


if __name__ == '__main__':
    if not os.path.exists('./data/index_components'):
        os.mkdir('./data/index_components')
        
    namespace = ['000300', '000016', '000905', '000906']
    for x in namespace:
        test = rqdatac.index_components(f'{x}.XSHG', start_date = '20050101', end_date=current_time)
        with open(f'./data/index_components/{x}.XSHG.pkl', 'wb') as f:
            pickle.dump(test,f)
    print(f'successfully processed! The updated file is saved to {path_current}/data/index')      

# with open('./data/index_components/test.pkl', 'rb') as f:
#     ff = pickle.load(f)
