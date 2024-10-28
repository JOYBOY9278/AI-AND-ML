import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cars = pd.read_csv('usedcars.csv').rename(columns=lambda x: x.strip())

print("Column names:", cars.columns)
print(cars.head())


sns.pairplot(cars)
plt.show()


sns.scatterplot(x='price', y='mileage', data=cars)
plt.xlabel('Price')
plt.ylabel('Mileage')
plt.show()


sns.scatterplot(x='year', y='price', data=cars)
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()


sns.relplot(x='year', y='price', data=cars, hue='transmission', col='transmission', col_wrap=2, palette='bright', height=3)
plt.show()


sns.barplot(x='color', y='price', data=cars, hue='transmission', palette='bright')
plt.xlabel('Color')
plt.ylabel('Price')
plt.show()


sns.boxplot(x='transmission', y='price', data=cars)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Transmission')
plt.ylabel('Price')
plt.show()

if 'fuel' in cars.columns:
    my_df = cars[cars['fuel'].isin(['diesel', 'petrol'])]
    sns.catplot(x='transmission', y='price', data=my_df, kind='violin', hue='transmission', col='fuel', palette='bright', height=4, aspect=1.5)
    plt.show()
