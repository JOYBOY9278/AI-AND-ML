import pandas as pd
import matplotlib.pyplot as plt
# DataFrame of each student and the votes they get
dataframe = pd.DataFrame({'Name': ['Aparna', 'Aparna', 'Aparna',
'Aparna', 
'Aparna', 'Juhi',
 'Juhi', 'Juhi', 'Juhi', 'Juhi',
 'Suprabhat', 'Suprabhat',
 'Suprabhat', 'Suprabhat',
 'Suprabhat'],
 'votes_of_each_class': [12, 9, 17, 19,
 20, 11, 15, 12,
 9, 4, 22, 19, 17,
 19, 18]})
# Plotting the pie chart for above dataframe
dataframe.groupby(['Name']).sum().plot(
kind='pie', y='votes_of_each_class',
autopct='%1.0f%%')
plt.title("UNIVARIATE COMPOSITION")
plt.show()
plt.title("UNIVARIATE DISTRIBUTION")
plt.hist(dataframe['votes_of_each_class'])
plt.show()
print("Mean:",dataframe['votes_of_each_class'].mean())
20
print("median:",dataframe['votes_of_each_class'].median())
print("Standrad deviation:",dataframe['votes_of_each_class'].std())
x=dataframe.Name
y=dataframe.votes_of_each_class
plt.title("UNIVARIATE COMPARISON")
plt.plot(x,y)
plt.show()
