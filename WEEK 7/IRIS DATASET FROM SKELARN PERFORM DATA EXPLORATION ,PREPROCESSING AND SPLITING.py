import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('Y:/AI and ML/Datasets/iris.csv')
print(df.head())

# Check for missing values
print(df.isnull().sum())
df['petal_length'].mean()
df['petal_length'].fillna(df['petal_length'].mean(), inplace=True)
print(df['petal_length'].isna().sum())

# Boxplot before IQR method
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.title('petal_length BEFORE IQR METHOD')
sns.boxplot(df['petal_length'])

# Calculate IQR
q1 = df['petal_length'].quantile(0.25)
q3 = df['petal_length'].quantile(0.75)
iqr = q3 - q1
upper_limit = q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)

# Replace outliers
df.loc[(df['petal_length'] > upper_limit), 'petal_length'] = upper_limit
df.loc[(df['petal_length'] < lower_limit), 'petal_length'] = lower_limit

# Boxplot after IQR method
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 2)
plt.title('petal_length AFTER IQR')
sns.boxplot(df['petal_length'])
plt.show()

# Prepare data for training and testing
x = df.drop(columns=['sepal_width'], axis=1)
y = df['sepal_width']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# Print the training and testing sets
print(x_train)
print(x_test)
print(y_train)
print(y_test)
