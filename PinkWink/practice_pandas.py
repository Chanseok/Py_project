#%%
import pandas as pd
import numpy as np

s = pd.Series([1,3,5, np.nan, 6,8])
s
#%%
dates = pd.date_range('20180703', periods=6)
dates

#%%
df = pd.DataFrame(np.random.randn(6,4), 
                index = dates, columns=['A', 'B', 'C', 'D'])
df
df.head()

df.index
df.columns
df.values

df.info()
df.describe()