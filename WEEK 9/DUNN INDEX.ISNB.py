import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math

data = pd.read_csv("y:\AI and ML\Datasets\Mall_Customers.csv")
print(data.head())


x = data.iloc[:, 3:5].values
km = KMeans(n_clusters=5)
y_means = km.fit_predict(x)

def max_intra_cluster_distance(cluster_points, centroid):
    max_dist = float('-inf')
    for point in cluster_points:
        dist = math.dist(centroid, point)
        if dist > max_dist:
            max_dist = dist
    return max_dist

max_distance = float('-inf')
centroids = km.cluster_centers_  
for i in range(0, 5):
    cluster_points = x[y_means == i]
    centroid = centroids[i]  
    dist = max_intra_cluster_distance(cluster_points, centroid)
    if dist > max_distance:
        max_distance = dist

print("Maximum intra-cluster distance:", max_distance)

def min_inter_cluster_distance(centroids):
    min_dist = float('inf')
    for i in range(len(centroids)):
        for j in range(len(centroids)):
            dist = math.dist(centroids[i], centroids[j])  
            if i == j:
                continue
            else:
                if dist < min_dist:
                    min_dist = dist
    return min_dist

min_inter_distance = min_inter_cluster_distance(centroids)
print("Minimum inter-cluster distance:", min_inter_distance)
