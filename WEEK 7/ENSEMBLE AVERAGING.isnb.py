import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb 

df = pd.read_csv("Datasets/usedcars.csv")  
target = df['price']
train = df.drop('price',axis=1) 
train = pd.get_dummies(train)


x_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.20)


model_1 = LinearRegression()
model_2 = xgb.XGBRegressor()  
model_3 = RandomForestRegressor()  


model_1.fit(x_train, y_train)
model_2.fit(x_train, y_train)
model_3.fit(x_train, y_train)


pred_1 = model_1.predict(x_test)
pred_2 = model_2.predict(x_test)
pred_3 = model_3.predict(x_test)


pred_final = (pred_1 + pred_2 + pred_3) / 3.0

print('mean_squared_error:',mean_squared_error(y_test, pred_final))
