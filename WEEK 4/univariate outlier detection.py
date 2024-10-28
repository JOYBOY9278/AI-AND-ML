import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('height.csv')
ax=sns.boxplot(x=df["Age"])
ax.set_xlabel("Age")
ax.set_ylabel("name")
ax.set_title("Age boxplot")
plt.show()

height_lq=df["Age"].quantile(0.25)
height_uq=df["Age"].quantile(0.75)
height_iqr=height_uq-height_lq
lower_bound=height_lq-1.5*height_iqr
upper_bound=height_uq+1.5*height_iqr
Height_outliers=df[(df.Age<=lower_bound)|(df.Age>=upper_bound)]
print(Height_outliers)
