import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
 x = iris.data
y = iris.target


df = pd.DataFrame(x, columns=iris.feature_names)
df['target'] = y
print(df)
print(df.dtypes)
print(df.info())


plt.scatter(df.index, df['petal width (cm)'])
plt.show()

sns.scatterplot(data=df,x=df.index, y='petal width (cm)', hue='target')
plt.show()

sns.swarmplot(data=df, x='petal width (cm)')
sns.swarmplot(data=df, y='petal width (cm)')
plt.show()

plt.hist(df['petal width (cm)'])
plt.show()

df['petal width (cm)'].plot(kind='density')
plt.show()

plt.boxplot(df['petal width (cm)'])
plt.show()
plt.boxplot(data=df, x='sepal width (cm)')
plt.show()

df['target'].value_counts().plot.bar()
plt.show()

sns.countplot(data=df, x='target')
plt.show()

plt.pie(df['target'].value_counts(), labels=iris.target_names)
plt.show()
