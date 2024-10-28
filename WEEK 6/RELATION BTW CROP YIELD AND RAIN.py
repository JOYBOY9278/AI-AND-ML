import pandas as pd 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import numpy as np  
df=pd.read_csv("Y:\AI and ML\Datasets\Crop_recommendation.csv") 
print(df.head())
df = df.dropna() #drop rows with missing values 

x=df[['CROP YIELD']] 
y=df[['RAINFALL RATE']]
plt.plot(x,y,color='g')
plt.show()

X=x.astype(float) 
Y=y.astype(float)
model=sm.OLS(Y,X).fit() 
print(model.summary())



plt.plot(x, model.predict(sm.add_constant(X)), color='red')
plt.xlabel('Crop Yield')
plt.ylabel('Rainfall Rate')
plt.title('Linear Regression Analysis')
plt.show()
