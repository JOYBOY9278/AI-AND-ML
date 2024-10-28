import os
import pandas as pd
import numpy as np

sal = pd.read_csv("Salary_Data.csv")
print("Count of Null values before imputation\n")
print(sal.isnull().sum())
sal.head()
sal.describe()

missing_col = ['Salary']
for i in missing_col:
    sal.loc[sal.loc[:, i].isnull(), i] = sal.loc[:, i].mean()
    print("Count of Null values after imputation\n")
    print(sal.isnull().sum())
sal
