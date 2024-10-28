import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


df = pd.read_csv("Y:\AI and ML\Datasets\Crop_recommendation.csv")


df = df.dropna()  # Drop rows with missing values


x = df[['CROP YIELD']]
y = df[['RAINFALL RATE']]
plt.plot(x,y)
plt.show()


X = x.astype(float)
Y = y.astype(float)


model = sm.OLS(Y, sm.add_constant(X)).fit()  # Add a constant term for the intercept
print(model.summary())

# Visualize the data
plt.scatter(x, y)
plt.plot(x, model.predict(sm.add_constant(X)), color='red')
plt.xlabel('Crop Yield')
plt.ylabel('Rainfall Rate')
plt.title('Linear Regression Analysis')
plt.show()
