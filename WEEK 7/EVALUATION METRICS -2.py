import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics, tree
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
iris_dataset = pd.read_csv(r"Y:/AI and ML/Datasets/iris.csv")
print(iris_dataset.head())
iris_dataset = iris_dataset.drop(labels = ['species'],axis=1)


iris_values = iris_dataset.values
X,y = iris_values[:,:-1], iris_values[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.5, 
random_state = 42)
classifier = tree.DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)


predictions = classifier.predict(X_test)
conf_matrix = metrics.confusion_matrix(y_test, predictions)
categories = ['iris-setosa','iris-versicolor','iris-virginica']
sns.heatmap(conf_matrix,
annot=True,cmap='YlOrRd',
xticklabels=categories, cbar=False)
plt.yticks(np.arange(3),categories)
plt.ylabel('True labels');
plt.xlabel('Predicted labels');
plt.title('Confusion matrix of Iris species classification');
plt.show()
print(metrics.classification_report(y_test, predictions, digits=3))
metrics.classification_report(y_test, predictions, digits=3, output_dict=True)
