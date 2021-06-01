import pandas as pd
data=pd.read_csv("news_info.csv",low_memory=False)
data=data.head(100)
data.to_csv("NLP_example.csv",index=False,encoding="utf-8")