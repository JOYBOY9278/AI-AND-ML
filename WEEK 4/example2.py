import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(f'iris.csv')
print(df.head(10))

plt.figure(figsize=(6,6))
plt.title('Line Plot of Petal Length')
plt.xlabel('Index', fontsize=20)
plt.ylabel('Petal Length', fontsize=20)
plt.plot(df.index, df['petal_length'], markevery=1, marker='d')
for name, group in df.groupby('variety'):
    plt.plot(group.index, group['petal_length'], label=name, markevery=1, marker='d')
plt.legend()
plt.show()

sns.set(rc={'figure.figsize':(7,7)})
sns.set(font_scale=1.5)
fig=sns.lineplot(x=df.index,y=df['petal_length'],markevery=1,marker='d',data=df,hue=df['variety'])
fig.set(xlabel='index')
plt.show()


sns.stripplot(y=df['sepal_width'])
plt.show()

sns.stripplot(x=df['variety'],y=df['sepal_width'])
plt.show()

sns.set(rc={'figure.figsize':(5,5)})
sns.swarmplot(x=df['sepal_width'])
plt.show()
        
sns.swarmplot(x=df['variety'],y=df['sepal_width'])
plt.show()
        
plt.hist(df['petal_width'])
plt.show()

plt.figure(figsize=(5,5))
df['petal_length'].plot(kind='density')
plt.show()

sns.set(rc={'figure.figsize':(5,5)})
sns.kdeplot(df['petal_length'],shade=True)
plt.show()

plt.boxplot(df['sepal_width'])
plt.show()

dfm=df.drop('variety',axis=1)
plt.figure(figsize=(9,9))
plt.title('box plots of the 4 variables')
plt.boxplot(dfm.values,labels=['sepal_lenght','sepal_width','petal_lenght','petal_width'])
plt.show()

sns.boxplot(df['sepal_width'])
plt.show()

sns.set(rc={'figure.figsize':(9,9)})
sns.boxplot(x="variable",y="value",data=pd.melt(dfm))
plt.show()

plt.figure(figsize=(7,7))
plt.violinplot(dfm.values,showmedians=True)
plt.show()

sns.set(rc={'figure.figsize':(5,5)})
sns.violinplot(df['sepal_width'],orient='vertical')
plt.show()

sns.set(rc={'figure.figsize':(9,9)})
sns.violinplot(x=df['variety'],y=df['petal_width'],data=df)
plt.show()


