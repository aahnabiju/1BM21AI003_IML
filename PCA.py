import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load iris dataset as an example
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data (optional but recommended for PCA)
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_standardized = (X - mean) / std

# Create a PCA instance and fit the data
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_standardized)

# Visualize the results
plt.figure(figsize=(8, 6))
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
