import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

df=pd.read_csv(r"iris.csv")
print(df)
fig=plt.figure()
x=df.sepal_length
y=df.petal_length
z=df.petal_width
ax=fig.add_subplot(111,projection='3d')
plt.title("Multiunivaraite Distribution")
ax.scatter(x,y,z, linewidth=1,alpha=.7,edgecolor='k',s=200,c=z)
ax.plot(x,y,z)
plt.show()
print("Multivariate Comparision")
fig= plt.figure()
ax = px.line_3d(df, x="petal_length", y="petal_width", z="sepal_length")
ax.show()

iris = datasets.load_iris()
X = iris.data
y = iris.target
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)
text_representation = tree.export_text(clf)
print(text_representation)
with open("decistion_tree.log", "w") as fout:
 fout.write(text_representation)
fig = plt.figure(figsize=(15,15))
_ = tree.plot_tree(clf, 
 feature_names=iris.feature_names, 
 class_names=iris.target_names,
 filled=True)
plt.title("MULTIVARIATE COMPOSTION")
plt.show()
