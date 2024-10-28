import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('mtcars.csv')
print(df.head(10))
print (plt.hist(x=df['msg']))
print(plt.scatter(x='wt',y='mpg',data=df))
print(df['am'].value_count().plot(kind='bar'))
print(sns.boxplot(df['mpg']))
print(df['mpg'].min())
print(df['mpg'].max())
                  
print(df['mpg'].quantile([.1,.25,.5,.75]))
                  
