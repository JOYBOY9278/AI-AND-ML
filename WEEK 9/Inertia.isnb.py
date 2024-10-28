import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('Datasets/Mall_Customers.csv')
data.head()

x = data.iloc[:, 3:5]

from sklearn.cluster import KMeans
wcss = []


for i in range(1, 11):
    kmeans = KMeans(n_clusters=i) 
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kml = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_mean = kml.fit_predict(x)  


plt.scatter(x[y_mean == 0].iloc[:, 0], x[y_mean == 0].iloc[:, 1], s=100, c='pink', label='C1:kanjoos')
plt.scatter(x[y_mean == 1].iloc[:, 0], x[y_mean == 1].iloc[:, 1], s=100, c='orange', label='C2:Average')
plt.scatter(x[y_mean == 2].iloc[:, 0], x[y_mean == 2].iloc[:, 1], s=100, c='green', label='C3:Bakar/Target')
plt.scatter(x[y_mean == 3].iloc[:, 0], x[y_mean == 3].iloc[:, 1], s=100, c='blue', label='C4:Pokiri')
plt.scatter(x[y_mean == 4].iloc[:, 0], x[y_mean == 4].iloc[:, 1], s=100, c='purple', label='C5:Intelligent')
plt.scatter(kml.cluster_centers_[:, 0], kml.cluster_centers_[:, 1], s=200, c='red', label='Centroids') 

plt.title('K Means Clusters')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

print("Inertia:", kml.inertia_)
print("Cluster Centers:", kml.cluster_centers_)
