import rqdatac
import os
import pickle
import tushare as ts
import time
import sys
import pandas as pd
import datetime
import requests
import json

rqdatac.init()
current_time = datetime.datetime.now().strftime("%Y%m%d")
path_current = os.getcwd()
if not os.path.exists(path_current + '/data'):
    os.mkdir(path_current + '/data')
if not os.path.exists('./data/index_components'):
    os.mkdir('./data/index_components')


if __name__ == '__main__':
        
    namespace = ['000300', '000016', '000905', '000906']
    for x in namespace:
        test = rqdatac.index_components(f'{x}.XSHG', start_date = '20050101', end_date=current_time)
        keys = pd.to_datetime(list(test.keys()))
        date = pd.to_datetime(list(test.keys())).strftime('%Y%m%d').to_list()
        res = pd.DataFrame(test.values(),index=pd.to_datetime(date))
        res.to_csv(f'./data/index_components/{x}.csv')
    print(f'successfully processed! The updated file is saved to {path_current}/data/index_components')      

# with open('./data/index_components/test.pkl', 'rb') as f:
#     ff = pickle.load(f)
