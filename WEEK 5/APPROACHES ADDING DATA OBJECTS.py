import pandas as pd
from numpy.random import randint
mark={'Name':['Harsha','Rakshitha','Manohar','Vidya'],
      'Maths':[87,98,87,95],'ITSKills':[83,99,84,76]}
df=pd.DataFrame(mark)
print (df)
df.loc[len(df.index)]=['Hruthvik',89,96]
print("\n",df)
