import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv("Y:\AI and ML\Datasets\height.csv")
ax=sns.boxplot(x=df["age"])
ax.set_xlabel("age")
ax.set_ylabel("name")
ax.set_title("age boxplot")
plt.show()

height_lq=df["age"].quantile(0.25)
height_uq=df["age"].quantile(0.75)
height_iqr=height_uq-height_lq

lower_bound=height_lq-1.5*heigght_iqr
upper_bound=height_uq+1.5*height_iqr
Height_outliers=df[(df.age<=lower_bound) | (df.age>=upper_bound)]
Height_outliers
