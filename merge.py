import pandas as pd
import tushare as ts
pro=ts.pro_api(token="53c01c697bd5f0a54b3ad025948d1491d4061ec9b4317870b1a3d795",timeout=30)
#获取申万一级行业列表
df1 = pro.index_classify(level='L1', src='SW')
#获取申万二级行业列表
df2 = pro.index_classify(level='L2', src='SW')
#获取申万三级级行业列表
df3 = pro.index_classify(level='L3', src='SW')
df1.to_csv("L1.csv",encoding="ANSI",index=False)
df2.to_csv("L2.csv",encoding="ANSI",index=False)
df3.to_csv("L3.csv",encoding="ANSI",index=False)