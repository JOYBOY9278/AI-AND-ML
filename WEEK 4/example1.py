import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
print(df.head(10))

plt.figure(figsize=(6.6))
plt.title('line plot of petal length')
plt.xlabel('index',fontsize=20)
plt.ylabel('petal length',fontsize=20)
plt.plot(df.index,df['petal.length']markevery=1,marker='d')
for name,group in df.groupby('variety'):
    plt.plot(group.index,group['petal.length'],label=name,markevery=1,marker='d')
plt.legend()
plt.show()
