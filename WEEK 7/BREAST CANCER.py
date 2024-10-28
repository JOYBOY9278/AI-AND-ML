import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('Y:/AI and ML/Datasets/breast-cancer.csv')
data.head()

x = data.drop(["diagnosis"], axis=1)
y = data["diagnosis"].values

#LABELENCODER
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

#SPLITING DATA 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)


score = dt.score(x_test, y_test)
print(f'Model Accuracy: {score}')
