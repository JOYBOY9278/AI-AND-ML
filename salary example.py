import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('Salary_Data.csv')
print(df.head(10))

df.isnull=True

sns.set_style('darkgrid')
sns.scatterplot(y=df['Salary'], x=df['YearsExperience'])
plt.title("Salary vs Experience", size=20)
plt.ylabel("Salary", size=12)
plt.xlabel("Experience", size=12)
plt.show()

sns.regplot(x=df['YearsExperience'], y=df['Salary'])
plt.title("Regression plot", size=20)
plt.ylabel("Salary", size=12)
plt.xlabel("Experience", size=12)
plt.show()

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)

regression = LinearRegression()
regression.fit(train_x, train_y)
print("------model trained------")
pred_y = regression.predict(val_x)

prediction = pd.DataFrame({'Experience': [i[0] for i in val_x],
 'Predicted Salary': pred_y})
print(prediction)

compare_salaries = pd.DataFrame({'Actual Salary': val_y,
 'Predicted Salary': pred_y})
print(compare_salaries)

plt.scatter(x=val_x, y=val_y, color='blue')
plt.plot(val_x,pred_y, color='black')
plt.title('Actual vs Predicted Salary', size=20)
plt.ylabel('Salary', size=12)
plt.xlabel('Experience', size=12)
plt.show()

print("Mean Absolute Error:", mean_absolute_error(val_y, pred_y))
