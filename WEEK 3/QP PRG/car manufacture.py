import pandas as pd
da={"mpg":[18,15,18,16,17],"cylinders":[8,8,6,4,8],
    "displacement":[307,350,318,304,302],
    "horsepower":[130,165,150,150,140],"weight":[3504,3693,3436,3433,3449],
    "acceleration":[12.0,11.5,11.0,12.0,10.5],
    "model year":[70,71,7080,70],
    "origin":[1,1,1,1,1],"car name":["cherolet","buick","plymounth","amc","ford"]}
df=pd.DataFrame(da)
print(df)
sa=df.describe()
ei=df[df["cylinders"]==8]
ye = df.groupby('model year')["model year"].count( ) 
print("Statistical details of dataset:\n",sa) 
print("\n Cars with 8 cylinders:\n",ei) 
print("\n Number of cars manufactured in each year:\n",ye) 

