from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd 
import matplotlib.pyplot as plt

# Load the dataset
X = pd.read_csv("Y:/AI and ML/Datasets/breast-cancer.csv")
y = X.pop('diagnosis')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

# Build the model
model = RandomForestClassifier()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.imshow(conf_matrix, cmap='binary', interpolation='None')
plt.colorbar()
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix')
plt.show()

# Display confusion matrix
confusion_matrix_df = pd.DataFrame(conf_matrix, index=['True Negative', 'True Positive'], columns=['Predicted Negative', 'Predicted Positive'])
print("\nConfusion matrix\n")
print(confusion_matrix_df)
print("\n")

# Calculate precision
precision = conf_matrix[1][1] / (conf_matrix[1][1] + conf_matrix[0][1]) if (conf_matrix[1][1] + conf_matrix[0][1]) != 0 else 0
print("\nPRECISION:\n")
print(precision)
print("\n")

# Calculate recall
recall = conf_matrix[1][1] / (conf_matrix[1][1] + conf_matrix[1][0]) if (conf_matrix[1][1] + conf_matrix[1][0]) != 0 else 0
print("\nRECALL:\n")
print(recall)
print("\n")

# Calculate F1 Score
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
print("\nF1_SCORE:\n")
print(f1_score)
