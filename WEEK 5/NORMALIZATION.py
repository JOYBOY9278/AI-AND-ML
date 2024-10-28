import pandas as panda 
import numpy as numpy 
import matplotlib.pyplot as plot 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
df = panda.read_csv("Y:\AI and ML\Datasets\Salaries.csv") 
print(df) 
print(df.shape) 
print(df) 
df.isnull().any() 
df.isnull().sum() 
df['Salary'] = df['Salary'].fillna(0) 
print(df) 
df['YearsExperience'] = df['YearsExperience'].fillna(0) 
print(df) 
from sklearn import preprocessing 
a=nump.array(df['YearsExperience']) 
print(a) 
print('\n') 
b=preprocessing.normalize([a]) 
print(b)
