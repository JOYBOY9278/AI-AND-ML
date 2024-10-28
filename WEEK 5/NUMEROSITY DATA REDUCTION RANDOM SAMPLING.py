import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


customer_df=pd.read_csv('Customer Churn.csv')
print(customer_df.shape)
print(customer_df.Churn.value_counts())

customer_df_rs=customer_df.sample(1000,random_state=1)
y=customer_df_rs['Churn']
Xs=customer_df_rs.drop(columns=['Churn'])
print(customer_df_rs.shape)
print(customer_df_rs.Churn.value_counts())


n,s=len(customer_df),1000
print(n,s)
r=s/n
print('Ratio of each Churn class in sample:',r)
sample_df=customer_df.groupby('Churn').apply(lambda sdf:sdf.sample(round(len(sdf)*r)))
print(sample_df.Churn.value_counts())
customer_df.Churn.value_counts().plot.bar()
sample_df.Churn.value_counts().plot.bar()
plt.show()

n,s=len(customer_df),500
sample_df=customer_df.groupby('Churn').apply(lambda sdf:sdf.sample(250))
print(sample_df.Churn.value_counts())
sample_df.Churn.value_counts().plot.bar()
plt.show()
print(sample_df)

