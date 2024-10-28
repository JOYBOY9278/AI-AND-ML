import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df =pd.read_csv("height.csv")
dff=sns.boxplot(x=df['age'],y=df['height'])
dff=set_title('bivariate outlier detection')
plt.show()
