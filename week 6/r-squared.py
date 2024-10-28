import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('user_data.csv')
print(df)

x=df.iloc[:,[2,3]].values
y=df.iloc[:,4].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
print(x_train[0:10,:])

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state=0)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix:\n",cm)

from sklearn.metrics import accuracy_score
print("Accuracy:",accuracy_score(y_test,y_pred))

plt.scatter(x='Age',y='EstimatedSalary',data=df)
plt.title('model(Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

from sklearn .metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print("MSE:%.2f"%(mse))

import math
rmse=math.sqrt(mse)
print("RMSE:%2f"%(rmse))

      
