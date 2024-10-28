import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("Y:\AI and ML\Datasets\datetemp2.csv")
print(df)

x=df.Temp
y=df.Date

plt.scatter(x,y,label="values of x&y")
plt.xlabel('temp')
plt.ylabel('date')
plt.title('scatter plot')
plt.show()
 
