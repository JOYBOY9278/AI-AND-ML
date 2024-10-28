import pandas as pd
import numpy as np
d={
    "Day":[1,2,3,4,5,6,7,8,9,10],
    "Steps":[4335,9552,7332,4504,5335,7552,8332,6503,8965,7689]}
df=pd.DataFrame(d)
print(df)
df["+1000 Steps"]=df["Steps"]+1000
print ("\n dataframe after adding 1000 steps:\n",df)
fi=df[df["Steps"]>7000]["Day"]
print ("\n days on which steps were >7000:\n",fi)
