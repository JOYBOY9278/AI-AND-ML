import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Define the data
y = pd.Series([1, 2, 3, 4, 3, 5, 4])
x = pd.Series([1, 2, 3, 4, 5, 6, 7])

# Calculate correlation
correlation = y.corr(x)
print(correlation)

# Scatter plot
plt.scatter(x, y)
plt.plot(np.unique(x), np.polyval(np.polyfit(x, y, 1), np.unique(x)), color='red')

# Load dataset and create heatmap
flights = sns.load_dataset("flights")
ax = sns.heatmap(flights.corr(), annot=True)

# Set font scale and create another heatmap
sns.set(font_scale=1.15)
plt.figure(figsize=(8, 4))
sns.heatmap(flights.corr(), cmap='RdBu_r', annot=True, vmin=-1, vmax=1)
plt.show()
