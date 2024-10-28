import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
customer_df=pd.read_csv('Y:\AI and ML\Datasets\Customer Churn.csv')
print(customer_df.shape)
print (customer_df.Churn.value_counts())
customer_df_rs=customer_df.sample(1000,random_state=1)
y=customer_df_rs['Churn']
Xs=customer_df_rs.drop(columns=['Churn'])
print(customer_df_rs.shape)
print(customer_df_rs.Churn.value_counts())
