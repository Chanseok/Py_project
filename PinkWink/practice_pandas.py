#%%
import pandas as pd
import numpy as np

s = pd.Series([1,3,5, np.nan, 6,8])
s
#%%
dates = pd.date_range('20180703', periods=6)
dates

#%%
df = pd.DataFrame(np.random.randn(6,4), \
                index = dates, columns=['A', 'B', 'C', 'D'])
df
df.head()

df.index
df.columns
df.values

df.info()
df.describe()
df.sort_values(by='B', ascending=False)

df['A']
df[['A','B']]
df[0:3]
df['20180703':'20180705']

df.loc[dates[0]]
df.loc['20180703']
df.loc[:,['A','B']]
df.loc['20180703':'20180705',['A','B']]
df.loc[dates[0], 'A']

## Github 반영 준비부터 해야 하지 않을까?