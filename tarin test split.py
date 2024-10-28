import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('iris.csv')

x=df.iloc[:,:-2]
y=df.iloc[:,-2]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=5,random_state=0)
print(x)
print("splitted",y)
