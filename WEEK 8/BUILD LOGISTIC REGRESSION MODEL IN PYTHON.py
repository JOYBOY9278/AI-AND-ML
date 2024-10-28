import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Y:/AI and ML/Datasets/iris.csv')
print(df)
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.scatter(df['sepal_length'],df['sepal_width'],color='green')
plt.scatter(df['sepal_length'],df['sepal_width'],color='red',)
plt.show()
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.scatter(df['sepal_length'],df['sepal_width'],color='red')
plt.scatter(df['petal_length'],df['petal_width'],color='blue')
plt.show()


from sklearn.model_selection import train_test_split
from sklearn import linear_model,metrics
x=df.drop(['species'],axis='columns')

y=df.species
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
model=linear_model.LogisticRegression()
model.fit(x,y)
model.score(x_test,y_test)
