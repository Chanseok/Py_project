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
                          parse_cols = 'B, D, G, J, N', 
                          #자치구, 합계, 한국인 계, 외국인 계, 65세이상고령자
                          encoding='utf-8')
# rename
pop_Seoul = pop_Seoul.rename ( 
    columns = { pop_Seoul.columns[0]: "구별",
                pop_Seoul.columns[1]: "인구수",
                pop_Seoul.columns[2]: "한국인",
                pop_Seoul.columns[3]: "외국인",
                pop_Seoul.columns[4]: "고령자"})
pop_Seoul.drop([0], inplace=True)

if False:
    pop_Seoul['구별'].unique()
    pop_Seoul[pop_Seoul['구별'].isnull()]
    pop_Seoul[pop_Seoul['구별'].isnull()].info()

pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100 
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100 
pop_Seoul.head()

if False:
    pop_Seoul.sort_values(by='고령자비율', ascending=False).head()
    pop_Seoul.sort_values(by='외국인비율', ascending=False).head()
    pop_Seoul.sort_values(by='고령자', ascending=False).head()
    pop_Seoul.sort_values(by='외국인', ascending=False).head()
    pop_Seoul.sort_values(by='인구수', ascending=False).head()

#%%
CCTV_Seoul = pd.read_csv('02_CCTVInSeoul.csv', encoding='utf-8')
# CCTV_Seoul.head()
# CCTV_Seoul.sort_values(by='소계', ascending=False).head()
CCTV_Seoul['최근증가율'] = ( CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                            CCTV_Seoul['2014년'] ) / CCTV_Seoul['2013년도 이전'] * 100
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head()
CCTV_Seoul = CCTV_Seoul.rename( columns= {CCTV_Seoul.columns[0]:'구별'})

#%%
data_result = pd.merge( CCTV_Seoul, pop_Seoul, on='구별' )
data_result.drop(['2013년도 이전', '2014년', '2015년', '2016년'], 
        axis = 1, inplace=True)
data_result.set_index('구별', inplace=True)
# data_result.head()

if False:
    np.corrcoef(data_result['고령자비율'], data_result['소계'])
    np.corrcoef(data_result['외국인비율'], data_result['소계'])
    np.corrcoef(data_result['인구수'], data_result['소계'])
    data_result.sort_values(by='소계', ascending=False).head()
    data_result.sort_values(by='인구수', ascending=False).head()
    # data_result.sort_values(by='고령자비율', ascending=False).head()

#%%
import matplotlib.pyplot as plt
import numpy as np

import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False 
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system.... sorry ~~~ ')

if False:
    data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize = (10,10))
    plt.show()

data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()


#%%
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

# 
data_result['오차'] = np.abs( data_result['소계'] - f1(data_result['인구수']))
df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()


plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98,
                df_sort.index[n], fontsize=15)

plt.xlabel('인구수')
plt.ylabel('인구당 CCTV 비율')

plt.colorbar()
plt.grid()
plt.show()





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

