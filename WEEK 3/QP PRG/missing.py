import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
da={
    'n':[1,2,3,4,5],'pencil':[300,350,np.nan,500,520],'textbooks':[250,350,300,420,500],
     'drawing_sheets':[100,200,200,np.nan,300],'Profits':[800,np.nan,10256,12000,18000]
    }
df=pd.DataFrame(da)
print(df)
sta=df.describe()
print("\nStatistics of the dataset:\n",sta)
su=df['Profits'].sum()
print("\nSum of Profits;\n",su)
mi=df.isna()
print("\nmissing values :\n",mi)
number_of_missing=df.isnull().sum()
print("\nmaximum value:\n",df['drawing_sheets'].max())
plt.plot(df['n'],df['Profits'],'^-',color='k')
plt.xlabel("numbers");
plt.ylabel("Profits")
plt.show()
