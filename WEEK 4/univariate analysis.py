import pandas as pd 
X = pd.Series([1,3,5,10,20]) 
Y = pd.Series([2,4,1,-2,12]) 
print("The covariance value: ", X.cov(Y))

import pandas as pd
import numpy as np  
data = pd.DataFrame(np.random.randint(0, 10, size=(5, 3)), columns=['A', 'B', 'C'])
data
d1=data.corr()
print(d1)

import pandas as pd
data = pd.read_csv("iris.csv") 
data
d=data.drop(['variety'],axis='columns')
print(d.corr())   


