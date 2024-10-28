import numpy as np
from sklearn.model_selection import train_test_split

x =np.array(range(1, 25)).reshape((12, 2))
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=8)
print("\n X_train",x_train)
print("\n X_test",x_test)
print("\n Y_train",y_train)
print("\n Y_test",y_test)
