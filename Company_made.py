import pandas as pd
data=pd.read_csv("company_label.csv")
temp_1=data[['sec_code','company_name']]
temp_1=temp_1.drop_duplicates()
print(temp_1.shape)
temp_1.to_csv("company.csv",index=False)
# import pandas as pd
# data=pd.read_csv("industry_label.csv",encoding="utf-8")
# data=data[['industry_code','industry_name']]
# temp_1=data.drop_duplicates()
# temp_1.to_csv("industry.csv",index=False)

# import pandas as pd
# data1=pd.read_csv('industry_label.csv')
# data2=pd.read_csv('company_label.csv')
# result = pd.merge(data1, data2, on='news_id')
# result=result[['sec_code','company_name','industry_code','industry_name']]
# result=result.drop_duplicates()
# print(result.shape)