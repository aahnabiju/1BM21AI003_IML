import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate a sample dataset
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# Visualize the dataset
plt.scatter(X[:, 0], X[:, 1], s=50, cmap='viridis')
plt.title('Generated Dataset')
plt.show()

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# Get cluster centers and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualize the clustered dataset
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-means Clustering')
plt.legend()
plt.show()
