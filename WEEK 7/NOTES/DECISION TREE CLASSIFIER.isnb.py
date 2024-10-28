import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import pandas as pd

data=load_iris()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=50, test_size=0.25)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

# Make predictions
y_pred= clf.predict(x_test)

# Print training data accuracy
print("train data accuracy:", accuracy_score(y_true=y_train, y_pred=clf.predict(x_train)))




# Print test data accuracy
print("test data accuracy:", accuracy_score(y_test, y_pred))
print(y_test)
print(y_pred)

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
plt.plot(x,y_test,color='blue',label='actual value')
plt.plot(x,y_pred,color='red',label='predicted value')
plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.title('Predictions vs True')
plt.legend()
plt.show()