import pandas as pd
df1=pd.read_csv("Y:\AI and ML\Datasets\stu1.csv")
df2=pd.read_csv("Y:\AI and ML\Datasets\stu2.csv")
print (df1.head())
print (df2.head())
df1['Name']='abc','xyz','pqr','klm'
print(df1.head())
df=pd.merge(df1,df2,on='student_id')
print(df.head())
