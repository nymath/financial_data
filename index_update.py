#! /Users/nymath/opt/anaconda3/bin/python

import numpy as np
import pandas as pd
import os
import tushare as ts
import warnings
warnings.filterwarnings('ignore')

path_current = os.getcwd()
if os.path.exists(path_current + '/data')==0:
    os.mkdir(path_current + '/data')
if os.path.exists('./data/index')==0:
    os.mkdir('./data/index')


if __name__ == '__main__':
    pro = ts.pro_api('91f8d52bdfeb4b1cb7191909907f211801b427289c9767155db02262')
    index_lst = ['000300.SH', '000905.SH', '000852.SH', '000016.SH']
    for x in index_lst:
        df = pro.index_daily(**{
            "ts_code": x,
            "start_date": "20050101",
        }, fields=["ts_code","trade_date","close","open","high","low","pre_close","change","pct_chg","vol","amount"]) 
        df.sort_values(['trade_date'],ignore_index=True,inplace=True)
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        df.to_csv(f'./data/index/{x}.csv',encoding='utf-8',index=False)
        
    df['pre_trade_date'] = df['trade_date'].shift(1)
    trade_date = df[['trade_date','pre_trade_date']]
    temp = pd.Series(trade_date['trade_date'])
    trade_date['year'] = temp.apply(lambda x:x.year)
    trade_date['month'] = temp.apply(lambda x:x.month)
    trade_date['week'] = temp.apply(lambda x:x.week)
    trade_date['quarter'] = temp.apply(lambda x:x.quarter)
    yearend = trade_date.drop_duplicates(['year'],keep='last')['trade_date']
    quaterend = trade_date.drop_duplicates(['year','quarter'],keep='last')['trade_date']
    monthend = trade_date.drop_duplicates(['year','month'],keep='last')['trade_date']
    weekend = trade_date.drop_duplicates(['year','week'],keep='last')['trade_date']
    trade_date.set_index('trade_date',inplace=True)
    trade_date['is_weekend'] = 0
    trade_date.loc[weekend,'is_weekend'] = 1
    trade_date['is_monthend'] = 0
    trade_date.loc[monthend,'is_monthend'] = 1
    trade_date['is_quarterend'] = 0
    trade_date.loc[quaterend,'is_quarterend'] = 1
    trade_date['is_yearend'] = 0
    trade_date.loc[yearend,'is_yearend'] = 1
    trade_date.to_csv('./data/index/trade_date.csv',encoding='utf-8')
    print(f'successfully processed! The updated file is saved to {path_current}/data/index')