import pandas as pd
market_name=['NY_EQ', 'QS_EQ', 'NQ_EQ', 'SH_EQ', 'HK_EQ', 'SZ_EQ']#各股市代码
data1=pd.read_csv('company_label.csv')
data2=pd.read_csv('industry_label.csv')
SH_market=data1.loc[data1['sec_code'].str.contains('SH_EQ')]
SZ_market=data1.loc[data1['sec_code'].str.contains('SZ_EQ')]
data1=pd.concat([SH_market,SZ_market],axis=0)
df=pd.merge(data2, data1, on='news_id',how='inner')
df.to_csv("temp.csv",index=False,encoding="ANSI")
company_code=[]
company_name=[]
company_industry=[]
temp=pd.read_csv("temp.csv",encoding="ANSI")
name=temp[['sec_code']]
name=name.drop_duplicates('sec_code')
name=name['sec_code'].tolist()
hangye_fenlei=temp.groupby('sec_code')
for i in range(0,len(name)):
    temp=hangye_fenlei.get_group(name[i])
    temp.to_csv("log.csv",encoding="ANSI",index=False)
    log=pd.read_csv("log.csv",encoding="ANSI")
    hangye=log.groupby('industry_code')['relevance_x'].sum()
    code=log.iloc[0,6]
    hangye=hangye.idxmax()
    company_code.append(code)
    company_name.append(name[i])
    company_industry.append(hangye)
result=pd.DataFrame({"company_code":company_code,
                     "company_name":company_name,
                     "company_industry":company_industry})
result.to_csv("industry.csv",index=False)