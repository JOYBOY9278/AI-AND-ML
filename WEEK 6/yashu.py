import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv("cricket.csv")

df1 = df.copy()
df1.isnull().sum()
corr = df1.corr()
plt.figure(figsize=(20, 10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
def correlation(dataset, threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                colname = corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr  # Return statement moved outside the loop

corr_features = correlation(df1, 0.7)
df1.drop(['SR', 'halfcentury', 'BF'], axis=1, inplace=True)
q1 = df['SR'].quantile(0.25)
q3 = df['SR'].quantile(0.75)
iqr = q3 - q1
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.title('SR')
sns.boxplot(df['SR'])
plt.subplot(1, 2, 2)
plt.title('SR')
sns.distplot(df['SR'])
x = df.drop(columns=['SR'], axis=1)
y = df['SR']
upper_limit = q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
