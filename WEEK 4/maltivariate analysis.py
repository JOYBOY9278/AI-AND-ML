import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(font_scale=1.3)
cars = pd.read_csv('usedcars.csv')
print("Column names:", cars.columns)
print(cars.head())
sns.pairplot(cars)
plt.show()
cars.columns = cars.columns.str.strip()
sns.scatterplot(
    x='price',
    y='mileage',
    data=cars
)
plt.xlabel('Price')
plt.ylabel('Mileage')
plt.show()
sns.pairplot(  
    data=cars,
    aspect=.85,
    hue='transmission')
sns.scatterplot(
    x='year',
    y='price',
    data=cars
)
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()
sns.scatterplot(
    x='year',
    y='price',
    data=cars
)
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()
sns.relplot(
    x='year',
    y='price',
    data=cars,
    hue='transmission',
    col='transmission',  
    col_wrap=2,
    palette='bright',
    height=3,
    aspect=1.3
)
plt.show()
sns.barplot(
    x='color',
    y='price',
    data=cars,
    color='blue'
)
plt.xlabel('Color')
plt.ylabel('Price')
plt.show()
sns.barplot(
    x='color',
    y='price',
    data=cars,
    hue='transmission',
    palette='bright'
)
plt.xlabel('Color')
plt.ylabel('Price')
plt.show()
g = sns.catplot(
    x='color',
    y='price',
    data=cars,
    kind='bar',
    hue='transmission',
    col='transmission', 
    col_wrap=2,
    palette='bright',
    height=3,
    aspect=1.3
)
g.set_titles('Transmission: {col_name}')
plt.show()
sns.boxplot(
    x='transmission',
    y='pri  ce',
    data=cars,
    color='blue'
)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Transmission')
plt.ylabel('Price')
plt.show()
g = sns.catplot(
    x='transmission',  
    y='year', 
    data=cars,
    kind='box',
    hue='transmission',
    col='color', 
    col_wrap=2,
    palette='bright',
    height=3,
    aspect=1.5
)
g.set_titles('Color: {col_name}')
g.set_xticklabels(rotation=45, ha='right')
plt.show()
sns.violinplot(
    x='transmission',
    y='price',
    data=cars,
    color='blue'
)
plt.xlabel('Transmission')
plt.ylabel('Price')
plt.show()
if 'fuel' in cars.columns:
    my_df = cars[cars['fuel'].isin(['diesel', 'petrol'])]
    g=sns.catplot(x='transmission',y='price', data=my_df,kind='violin',hue='transmission',col='fuel',palette='bright',height=4,aspect=1.5)
    g.set_xticklabels(rotation=90)
plt.show()

my_df = cars[cars['fuel'].isin(['diesel', 'petrol'])]

if not my_df.empty and all(col in my_df.columns for col in ['owner', 'engine_cc', 'transmission']):
    g = sns.catplot(
        x="owner",
        y="engine_cc",
        data=my_df,
        palette='bright',
        kind='violin',
        hue="transmission",
        col='fuel'
    )
g.set_xticklabels(rotation=90)
plt.show()
