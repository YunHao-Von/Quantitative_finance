# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:46:59 2020

@author: DELL
"""
import pandas as pd
import datetime
year=['2017','2018','2019','2020']#设置年份
# month=[('0101','0331'),('0401','0630'),('0701','0930'),('1001','1231')]#设置时间段
m=['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']#设置月份
def get__score(df_basic_filled_list,d,t):#对单一指标进行排序
    df=df_indicator_filled_list
    df=df_indicator_filled_list[t[0:4]][t[4:]]
    df=df.loc[:,['ts_code',d]]
    dg=df.groupby('ts_code')
    dg=dg.mean()
    dg=dg.sort_values(d,ascending=False)
    rank=dg.rank()
    return rank
def unit_socre(df,ind,t):#联合单一指标获得联合指标排序
    tmp=get__score(df,ind[0],t)
    rank=tmp
    for i in range(1,len(ind)):
        tmp=get__score(df,ind[i],t)
        rank = pd.merge(rank,tmp,how='inner',on='ts_code')
    rank['score']=rank.apply(lambda x:x.sum(),axis=1)
    return rank
# =============================================================================
#step1.读取数据 
# =============================================================================
#df_indicator=pd.read_csv('D:\\金融建模\\数据\\import_data\\fin_indicator.csv')#读入数据
#df_indicator=pd.read_csv('D:\\金融建模\\数据\\import_data\\table.csv')#读入数据
df_indicator=pd.read_csv('daily_basic.csv')#读入数据
#df_basic=df_basic.loc[:,['ann_date','total_share','ts_code']]
# =============================================================================
# step2.数据基本处理
# =============================================================================
df_indicator_filled=df_indicator.fillna(0)#填充空缺
df_indicator_filled['trade_date']=pd.to_datetime(df_indicator_filled['trade_date'],format='%Y%m%d')#设置时间戳
df_indicator_filled=df_indicator_filled.set_index('trade_date')#设置index为时间序列
df_indicator_filled_list={}#字典保存按年份和月份分割的Dataframe
# =============================================================================
# step3.划分数据生成字典
# =============================================================================
for i in year:
    month_dict={}
    for j in m:
        month_dict[j]=df_indicator_filled.loc[i+j,:]
    df_indicator_filled_list[i]=month_dict
# =============================================================================
# 设置指定指标
#fina_indicator=['roa','roe','debt_to_assets','bps']#选取的指标
#table=['total_share']
daily=['pe','pb','ps','total_mv']
# =============================================================================
score_indicator=unit_socre(df_indicator_filled_list,daily,'2017-04')#获得指定指标序列和指定时间的打分
select=score_indicator.sort_values(by='score',ascending=False).head(100)
print(select.index)
print(select)
# t='2020-06'
# d='roa'
# df=df_indicator_filled_list
# df=df_indicator_filled_list[t[0:4]][t[4:]]
# df=df.loc[:,['ts_code',d]]
# dg=df.groupby('ts_code')
# dg=dg.mean()
# dg=dg.sort_values(d,ascending=False)
# rank=dg.rank()
# rank=pd.DataFrame(index=)
# for i in fina_indicator:
#     tmp=get__score(df,i,t)
#     rank = pd.merge(rank,tmp,how='inner',on='ts_code')