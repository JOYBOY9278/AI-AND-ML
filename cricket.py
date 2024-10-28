import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("cricket.csv")
df['SR']=pd.to_numeric(df['SR'],errors='coerce')
print(df.head())
print(df.describe())
print(df.info())

df1=df.copy()
df1

df1.isnull().sum()
corr=df1.corr()
plt.figure(figsize=(20,10))
sns.heatmap(corr,annot=true,cmap='collwarm')
def correlation(dataset,thershould):
    col_corr=set()
    corr_matrix=dataset.corr()
    for i in range(len(corr_matrix.coiumns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j])>threshould:
                colname=corr_matrix.columns[i]
                col_corr.add(colname)
returncol_corr
corr_feature=correlation(df1,0.7)
len(set(corr_features))

corr_features

df1.drop(['SR','halfcentury','BF'],axis=1,inplace=true)
df1

q1=df['SR'].quantile(0.25)
q3=df['SR'].quantile(0.75)
iqr=q3-q1
q1,q3,iqr

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title('SR')
sns.boxplot(df['SF'])
pit.subplot(1,2,2)
plt.title('SR')
sns.distplot(df['SR'])
x=df.drop(columns=['SR'],axis=1)
y=df['SR']
upper_limit=q3+(1.5*iqr)
lower_limit=q1-(1.5*iqr)
upper_limit,lower_limit
x
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=5)
x_train
y_train 
