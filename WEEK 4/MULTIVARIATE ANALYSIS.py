import pandas as pd
import numpy as np
x=pd.Series([1,3,5,10,20])
y=pd.Series([2,4,2,1,-2,12])
print("the converiance value:",x.cov(y))


import pandas as pd
data=pd.read_csv('iris.csv')
data
data.corr()


data=pd.DataFrame(np.random.randit(0,10,size=(5,3)),columns=['A','B','C'])
data
data.corr()
