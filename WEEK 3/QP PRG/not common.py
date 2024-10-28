import pandas as pd
a = pd.Series([10,20,30,40,50])
b = pd.Series([40,50,60,70,80])

print ("Series A:",a)
print ("\nSeries B :",b)

not_com=a[~a.isin(b)].tolist()+b[~b.isin(a)].tolist()
print("item not common to both series:")
print (not_com)
print("\nLargest element in series A:\n",a.max())
print("\nsmallest element in series A:\n",a.min())
print ("\nsum of series B:\n",b.sum())
print("\naverage of series A:\n",a.mean())
print("\nmedian of series b:\n",a.median())
