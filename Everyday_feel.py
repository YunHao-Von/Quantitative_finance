import pandas as pd
import datetime
year=['2017','2018','2019','2020']#设置年份
m=['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']#设置月份
df_indicator=pd.read_csv('daily_basic.csv')
df_indicator_filled=df_indicator.fillna(0)#填充空缺
df_indicator_filled['trade_date']=pd.to_datetime(df_indicator_filled['trade_date'],format='%Y%m%d')#设置时间戳
df_indicator_filled=df_indicator_filled.set_index('trade_date')#设置index为时间序列
df_indicator_filled_list={}#字典保存按年份和月份分割的Dataframe
for i in year:
    month_dict={}
    for j in m:
        month_dict[j]=df_indicator_filled.loc[i+j,:]
    df_indicator_filled_list[i]=month_dict
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
daily=['pe','pb','ps','total_mv']
score_indicator=unit_socre(df_indicator_filled_list,daily,'2017-04')#获得指定指标序列和指定时间的打分
select=score_indicator.sort_values(by='score',ascending=False).head(100)
l=select.index.to_list()
data=pd.read_csv("company_label.csv")
import re
data["code"]=data["sec_code"].apply(lambda x:re.findall(r"(.+)_.+_.+",x)[0]+"."+re.findall(r".+_(.+)_.+",x)[0])
data1=data[data["code"].isin(l)]
data1["time"]=pd.to_datetime(data1["news_time"])
t=pd.DataFrame(columns=["pos","neg","neu","公司","code"])
for i in data1["code"].unique():
    t1=data1[data1["code"]==i]
    t1.index=data1[data1["code"]==i]["time"]
    t2=t1.resample("1d")["pos","neg","neu"].mean()
    t2["code"]=i
    t2["公司"]=data1[data1["code"]==i].company_name.unique()[0]
    t=pd.concat([t,t2])
t.fillna(0,inplace=True)
import numpy as np
df=pd.read_csv("event_label.csv")
event=df.merge(data1,on="news_id",how="right")
for i in event["event_name"].unique()[1:]:
    event[i]=event["event_name"].apply(lambda x :1 if x==i else 0)
    event[i]=event[i].astype(np.uint8)
ls=list(event.columns[13:])
ls.append("公司")
ls.append("code")
len(event.code.unique())
T=pd.DataFrame(columns=ls)
for i in event["code"].unique():
    T1=event[event["code"]==i]
    T1.index=event[event["code"]==i]["time"]
    T2=T1.resample("1d")[list(event.columns[13:])].sum()
    T2["code"]=i
    T2["公司"]=event[event["code"]==i].company_name.unique()[0]
    T=pd.concat([T,T2])
t['datetime']=t.index
T['datetime']=T.index
t.to_csv("smallt.csv",index=False)
T.to_csv("bigt.csv",index=False)
# final=pd.concat([t,T.iloc[:,:-2]],axis=1)
# final.to_csv("final.csv",index=True)
# final['time']=final.index
# final.to_csv('final_time.csv',index=False)