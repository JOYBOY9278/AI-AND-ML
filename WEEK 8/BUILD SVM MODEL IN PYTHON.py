import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Load the dataset
df = pd.read_csv('Y:/AI and ML/Datasets/iris.csv')
print(df)

# Scatter plot for sepal dimensions
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.scatter(df['sepal_length'], df['sepal_width'], color='green')
plt.show()

# Scatter plot for petal dimensions
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.scatter(df['petal_length'], df['petal_width'], color='red')
plt.show()

# Prepare data for training
x = df.drop(['species'], axis='columns')
y = df['species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= None)

# Train the model
model = SVC()
model.fit(x_train, y_train)
print("Model Score:", model.score(x_test, y_test))

# Confusion matrix
y_true = [0, 0, 0, 1, 1, 1]
y_pred = [0, 0, 1, 1, 1, 1]
conf_matrix = confusion_matrix(y_true, y_pred)

plt.imshow(conf_matrix, cmap='binary', interpolation='None')
plt.colorbar()
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()

confusion_matrix_df = pd.crosstab(y_true, y_pred, rownames=['True'], colnames=['Predicted'])
print("\nConfusion Matrix:\n")
print(confusion_matrix_df)

# Precision and Recall
precision = confusion_matrix_df[1][1] / (confusion_matrix_df[1][1] + confusion_matrix_df[0][1])
print("\nPrecision:\n", precision)

recall = confusion_matrix_df[1][1] / (confusion_matrix_df[1][1] + confusion_matrix_df[1][0])
print("\nRecall:\n", recall)

# F1 Score
f1_score = 2 * (precision * recall) / (precision + recall)
print("\nF1 Score:\n", f1_score)

