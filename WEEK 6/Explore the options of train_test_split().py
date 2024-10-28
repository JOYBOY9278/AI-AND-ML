# import modules 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
# read the dataset 
df = pd.read_csv("Y:\AI and ML\Datasets\iris.csv") 
# get the locations 
X = df.iloc[:, :-2] 
y = df.iloc[:, -1] 
# split the dataset 
X_train, X_test, y_train, y_test = train_test_split( 
X, y, test_size=0.05, random_state=0) 
print(X) 
print("splitted",y)
