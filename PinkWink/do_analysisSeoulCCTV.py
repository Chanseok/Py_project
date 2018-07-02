#%%
import os
import pandas as pd

fJupyter = True
if fJupyter:
    os.chdir("c://Projects//Py_project//PinkWink")
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read raw data
pop_Seoul = pd.read_excel('01_PopulationInSeoul.xls',
                          header=2,
                          parse_cols = 'B, D, G, J, N', #자치구, 합계, 한국인 계, 외국인 계, 65세이상고령자
                          encoding='utf-8')
# rename
pop_Seoul = pop_Seoul.rename (index=str, columns = { pop_Seoul.columns[0]: "구별",
                pop_Seoul.columns[1]: "인구수",
                pop_Seoul.columns[2]: "한국인",
                pop_Seoul.columns[3]: "외국인",
                pop_Seoul.columns[4]: "고령자"})

pop_Seoul.head()

#%%
CCTV_Seoul = pd.read_csv('02_CCTVInSeoul.csv', encoding='utf-8')
CCTV_Seoul.head()

# print (pop_Seoul.head())
# print (CCTV_Seoul.head())

#########################
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import numpy as np

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()

# #%%
# print("Hello World ")
