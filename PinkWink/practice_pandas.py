#%%
import pandas as pd
import numpy as np

s = pd.Series([1,3,5, np.nan, 6,8])
s
#%%
dates = pd.date_range('20180703', periods=6)
dates

### Pandas 기본 사용법 익히기 
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

df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1,2,4],[0,3]]
df.iloc[1:3, :]
df.iloc[:, 1:3]

df.A
df[df.A>0]
df[df>0]

df2 = df.copy()
df2['E'] = ['one','one', 'two', 'three', 'four', 'four']
df2

df2['E'].isin(['two','four'])
df2[df2['E'].isin(['two','four'])]

df
df.apply(np.cumsum)

df.describe()
df['A'].max() - df['A'].min()
df.apply(lambda x: x.max() - x.min())

#%%
### Pandas 고급 기능 - 두 DataFrame 병합하기  
df1 = pd.DataFrame( {   'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']}, 
                        index = [0,1,2,3])

df2 = pd.DataFrame( {   'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']}, 
                        index = [4,5,6,7])
df3 = pd.DataFrame( {   'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']}, 
                        index = [8,9,10,11])
df4 = pd.DataFrame( {   'B': ['B2', 'B3', 'B6', 'B7'],
                        'D': ['D2', 'D3', 'D6', 'D7'],
                        'F': ['C2', 'C3', 'C6', 'C7']}, 
                        index = [2,3,6,7])
#%%
df1
df2
df3

result = pd.concat([df1, df2, df3])
result

result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
result
result.index
result.index.get_level_values(0)
result.index.get_level_values(1)

result = pd.concat([df1, df4], axis=0)
result

result = pd.concat([df1, df4], axis=1)
result

result = pd.concat([df1, df4], axis=1, join='inner')
result

result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
result

result = pd.concat([df1, df4], ignore_index=True)
result

#%%
left = pd.DataFrame( {'key': ['K0', 'K4', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left, right, on='key')
pd.merge(left, right, how='left',  on='key')
pd.merge(left, right, how='right', on='key')
pd.merge(left, right, how='outer', on='key')
pd.merge(left, right, how='inner', on='key')








