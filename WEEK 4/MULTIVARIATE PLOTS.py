import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

df = pd.read_csv('iris.csv')  

fig = plt.figure()
x = df['sepal_length']
y = df['petal_length']
z = df['petal_width']
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, linewidth=1, alpha=0.7, edgecolor='k', s=200, c=z)
plt.title("Multivariate Distribution") 
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Petal Length')
ax.set_zlabel('Petal Width')
plt.show()

print("Multivariate Comparison")
fig = px.scatter_3d(df, x='petal_length', y='petal_width', z='sepal_length')
fig.show()

print("Multivariate Relationship")
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_width', y='sepal_length', z='petal_width', size='petal_length', color='species')
fig.show()

iris = datasets.load_iris()
X = iris.data
y = iris.target
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)
text_representation = tree.export_text(clf)
print(text_representation)

with open("decision_tree.log", "w") as fout:  
    fout.write(text_representation)

fig = plt.figure(figsize=(15, 15))
_ = tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Multivariate Composition") 
plt.show()
