import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('BostonHousing.csv')
print(df.head())

d=df.isnull().sum()
print(d)
df.rad.mean()
df.crim.fillna(df.crim.mean(),inplace=True)
df.isnull().sum()
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title("zn")
sns.boxplot(df.zn)
plt.subplot(1,2,2)
plt.title("zn")
sns.distplot(df.zn)
plt.show()
sns.show()

q1=df.zn.quantile(0.25)
q3=df.zn.quantile(0.75)
iqr=q3-q1
upper_limit=q3+(1.5*iqr)
lower_limit=q1-(1.2*iqr)

df.loc[(dfzn>upper_limit)|(df.ZN<lower_limit)]
df.loc[(df.zn>upper_limit,"zn")]=upper_imit
df.loc[(df.zn>lower_limit,"zn")]=lower_imit
x=df.drop(columns=['medv'],axis=1)
y=df['medv']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
