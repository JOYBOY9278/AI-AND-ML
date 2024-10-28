import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s
data=pd.read_csv("mtcars.csv")
mpg=data['mpg']
plt.hist(mpg,bins='auto',color='g',edgecolor='c')
plt.xlabel('mile per gallon(mpg)');
plt.ylabel('frequency')
plt.title('frequency distribution of mpg')
plt.show()
wt=data['wt']
iv=range(len(data))
plt.scatter(iv,mpg,color='k',label='mpg')
plt.scatter (iv,wt,color='g',label='wt')
plt.title("relation between weight and mpg")
plt.legend()
plt.show()
c=data['am'].value_counts()
co=['k','g']
plt.bar(c.index,c.values,color=co,width=0.3)
plt.xticks([0,1],['0-Automatic','1-Manual'])
plt.xlabel("transmisson type")
plt.ylabel("no of cars")
plt.title("frequency distribution of transmission type of cars")
plt.show()
s.boxplot(mpg,color='c')
plt.xlabel("mpg")
plt.ylabel("value")
plt.title("box plot of mpg values ")
plt.show()
