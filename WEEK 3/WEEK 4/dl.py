import pandas as pd
data = pd.read_csv('iris.csv') 
data 
dl=data.corr()
print(dl)
