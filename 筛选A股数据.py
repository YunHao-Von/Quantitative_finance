# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:18:29 2020

@author: DELL
"""
import pandas as pd
import numpy as np
market_name=['NY_EQ', 'QS_EQ', 'NQ_EQ', 'SH_EQ', 'HK_EQ', 'SZ_EQ']#各股市代码
df=pd.read_csv('company_label.csv')
SH_market=df.loc[df['sec_code'].str.contains('SH_EQ')]
SZ_market=df.loc[df['sec_code'].str.contains('SZ_EQ')]
A_market=pd.concat([SH_market,SZ_market],axis=0)
code=A_market['sec_code'].apply(lambda x:x[0:6])
A_market['code']=code.values
A_market.to_csv('new_company_label.csv')
new_df=pd.DataFrame()
new_df['stock_code']=code.values
new_df['news_id']=A_market['news_id'].values
new_df.to_csv('id_info.csv',index=False)