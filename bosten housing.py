import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('BostonHousing.csv')
print(df)
print(df.head())

d1=df.isnull().sum()
print(d1)
df['crim'].fillna(df['crim'].mean(), inplace=True)

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.title("zn")
sns.boxplot(x=df['zn'])
plt.subplot(1, 2, 2)
plt.title("zn")
sns.distplot(df['zn'])
plt.show()


from sklearn.model_selection import train_test_split
x=df.iloc[:,2].values
y=df.iloc[:,3].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)
