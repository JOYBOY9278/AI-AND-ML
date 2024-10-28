

import pandas as pd 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import numpy as np 
df = pd.read_csv("Crop_recommendation.csv")
print(df.head())
df = df.dropna()  # Drop rows with missing values 
x = df['ph']
y = df['rainfall']
X = x.astype(float) 
Y = y.astype(float)
model = sm.OLS(Y, sm.add_constant(X)).fit()   
print(model.summary()) 
plt.plot(x,y)
plt.show() 

# Visualize the data 
plt.scatter(x, y) 
plt.plot(x, model.predict(sm.add_constant(X)), color='red') 
plt.xlabel('Crop Yield') 
plt.ylabel('Rainfall Rate') 
plt.title('Linear Regression Analysis') 
plt.show()

