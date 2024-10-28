import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

data = load_iris()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=50, test_size=0.25)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

# Make predictions
y_pred = clf.predict(x_test)

# Print training data accuracy
print("train data accuracy:", accuracy_score(y_true=y_train, y_pred=clf.predict(x_train)))

# Print test data accuracy
print("test data accuracy:", accuracy_score(y_test, y_pred))
print("True values:", y_test)
print("Predicted values:", y_pred)

# Corrected scatter plot
plt.scatter(y_test, y_pred, color='blue', label='Predictions')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('Predictions vs True Values')
plt.legend()
plt.show()
