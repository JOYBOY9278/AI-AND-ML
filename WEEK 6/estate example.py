import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df=pd.read_csv(f'Book1.csv')
print(df.head(10))
sns.scatterplot(x=df['SqFt'],y=df['Price'])
plt.title("Price vs Area",size=20)
plt.ylabel("Price",size=12)
plt.xlabel("Area",size=12)
plt.show()
sns.regplot(x=df['SqFt'],y=df['Price'])
plt.title("Regression Plot",size=20)
plt.ylabel("Price",size=12)
plt.xlabel("Area",size=12)
plt.show()

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
train_x,val_x,train_y,val_y=train_test_split(x,y,random_state=0)
regression=LinearRegression()
regression.fit(train_x,train_y)
print("----Model trained----")

pred_y=regression.predict(val_x)
prediction=pd.DataFrame({'Area':[i[0] for i in val_x],'Predicted Price':pred_y})
print(prediction)
compare=pd.DataFrame({'Actual price':val_y,'Predicted Price':pred_y})
print(compare)
plt.scatter(x=val_x ,y=val_y ,color='r')
plt.plot(val_x,pred_y,color='B')
plt.title('Actual vs Predicted price',size=20)
plt.ylabel('price',size=12)
plt.xlabel('Area',size=12)
plt.show()
print("Mean Absolute Error",mean_absolute_error(val_y,pred_y))
            
