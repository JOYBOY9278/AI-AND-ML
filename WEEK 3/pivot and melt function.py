import pandas as pd

d1 = {"Name":["patil","keerthi","yukthi"],"ID":[1,2,3],"Role":["CEO","Editor","Author"]}
df = pd.DataFrame(d1)
print(df)
print("\n")
df_melted = pd.melt(df)
print(df_melted)
df_pivote=df.pivot(columns = 'ID')
print(df_pivote)
