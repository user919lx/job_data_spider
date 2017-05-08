import pandas as pd
import numpy as np


df = pd.read_excel("json_excel.xls")
df.drop_duplicates(inplace=True)
# t = df['companySize'].value_counts()
t = df.pivot_table(values='positionId', index=['city'], columns=['companySize'], aggfunc=len,margins=True).sort_values(by=['All'], ascending=False)
cols = ['少于15人', '15-50人', '50-150人', '150-500人', '500-2000人', '2000人以上', 'All']
# print(t[cols])
# print(df['positionId'].count())

# print(df['positionId'].count())
# print(df.count())
# print(df['city'].value_counts())
# print(df['workYear'].value_counts())
# print(df['firstType'].value_counts())
print(df['companyShortName'].value_counts())