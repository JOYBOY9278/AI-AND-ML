import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
mi=df.isna()
print("missing values:\n",mi)
