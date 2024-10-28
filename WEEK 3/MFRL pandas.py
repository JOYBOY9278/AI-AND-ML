import pandas as pd
from operator import add
from functools import reduce

Coding={'subject':['python','java'],'amount':[1000,2000]}
df=pd.DataFrame(Coding)
print(df)
print("\n map operation to multiply amount by 2\n")
df['amount']=df['amount'].map(lambda x:x*2)
print(df)
print("\n")

print("opeartion of filter to display only subject column\n")
df2=df.filter(items=['subject'])
print(df2)
print("reduce operation to find total amount\n")
total_amount=reduce(add,df['amount'])
print(total_amount)
