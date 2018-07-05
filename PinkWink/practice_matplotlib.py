
#%%
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

plt.figure
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,12, 0.01)
# y = np.sin(t)
# dy = np.diff(y) # np.diff() 차분 함수 
# dy = np.insert(dy, 0, 0) / 0.01 

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), 'g', lw = 3, linestyle ='dashed', label = 'sin') # lw - line weight, 'g' - color = 'green'
plt.plot(t, np.cos(t), 'r', label = 'cos')
plt.grid()
plt.legend()
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("Example - Sinewave")
plt.show()

# y[0:3]
# dy[1:4]
# y[2] - y[1]
# %whos
# g = np.array([1, 2, 4, 10, 13, 20]) # http://rfriend.tistory.com/tag/%EC%B0%A8%EB%B6%84
# np.diff(g)  # [2-1, 4-2, 10-4, 13-10, 20-13]

#%%
import matplotlib.pyplot as plt
import numpy as np
t = [0,1,2,3,4,5,6]
y = [-1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
plt.plot(t,y, color='green', linestyle ='dashed', marker='o',
            markerfacecolor ='blue', markersize='8')
plt.grid()
plt.xlim([-0.5, 6.5])
plt.ylim([-2, 11.5])
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
t1 = np.array([0,1,2,3,4,5,6,7,8,9])
y1 = np.array([9,8,7,9,8,3,4,3,2,4])
plt.figure(figsize=(10,6))
plt.scatter(t1,y1, s=50,  c=y1, marker='>')
plt.colorbar()
plt.show()

#%%
s1 = np.random.normal(loc=0.0, scale=1.0, size=1000) # loc - 평균, scale - 표준편차
s2 = np.random.normal(loc=5.0, scale=0.5, size=1000)
s3 = np.random.normal(loc=10.0, scale=2, size=1000)

plt.figure(figsize=(10,6))
plt.plot(s1, label = 's1')
plt.plot(s2, label = 's2')
plt.plot(s3, label = 's3')
plt.legend()
plt.show()

#%%
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.grid()
plt.show()
















