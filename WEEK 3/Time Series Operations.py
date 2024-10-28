import pandas as pd
import numpy as np
df=pd.DataFrame({"Date":pd.date_range(start="2022-11-01",periods=21,freq="D"),"temp":np.random.randint(18,30,size=21)})
print(df.head())
df['temp_lag_1']=df['temp'].shift(1)
print("\nShift Function\n",df.head())
df_weekly=df.resample("W",on="Date").mean()
print("\nResample Function \n",df_weekly.head())
