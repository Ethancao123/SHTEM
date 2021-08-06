import math
import matplotlib
import matplotlib.pyplot as plt
import pandas as panda
import numpy as np

arr = []

df = panda.read_csv('data.csv', index_col=0)
count = 0
total = 0
for i in range(10000-1):
    if(count == 10):
        arr.append(total/10)
        count = 0
        total = 0
    count += 1
    total += df.iloc[i,0]
     
plt.plot(range(0,100000-100,100),arr)
plt.show()
print(arr)