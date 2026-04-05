# Day 26: K-Means Clustering, PCA, and Unsupervised Learning

## Unsupervised Learning Overview

In unsupervised learning, we work with **unlabeled data**. The goal is to discover
hidden structure, patterns, or groupings without predefined categories.

**Main applications:**
- **Clustering**: Group similar data points together
- **Dimensionality Reduction**: Compress many features into fewer, meaningful ones
- **Anomaly Detection**: Identify unusual data points
- **Association Rule Learning**: Find relationships between items

---

## K-Means Clustering

K-Means partitions data into **K clusters**, where each point belongs to the cluster
with the nearest center (centroid).

### Algorithm Steps

1. Choose K (number of clusters).
2. Randomly initialize K centroids.
3. **Assign** each point to the nearest centroid.
4. **Update** each centroid to the mean of its assigned points.
5. Repeat steps 3-4 until centroids stop moving (convergence).

### Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data with 4 clusters
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)

labels = kmeans.labels_           # Cluster assignments
centroids = kmeans.cluster_centers_  # Cluster centers
inertia = kmeans.inertia_         # Sum of squared distances to centroids

print(f"Cluster sizes: {np.bincount(labels)}")
print(f"Inertia: {inertia:.2f}")

# Visualize
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
```

### Choosing K: The Elbow Method

Plot inertia for different K values. The "elbow" where the curve bends is often a good choice.

```python
inertias = []
K_range = range(1, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
```

### Silhouette Score

Measures how similar a point is to its own cluster vs. other clusters. Ranges from
-1 (wrong cluster) to 1 (well clustered).

```python
from sklearn.metrics import silhouette_score, silhouette_samples

for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    score = silhouette_score(X, labels)
    print(f"K={k}: Silhouette Score = {score:.4f}")
```

### Limitations of K-Means

- Assumes **spherical clusters** of similar size
- Sensitive to **initial centroids** (use n_init > 1 or k-means++)
- Must specify K in advance
- Sensitive to **outliers**
- Cannot find non-convex clusters

---

## DBSCAN: Density-Based Clustering

DBSCAN does not require specifying the number of clusters and can find clusters of
arbitrary shape.

**Key parameters:**
- `eps`: Maximum distance between two points in the same neighborhood
- `min_samples`: Minimum points to form a dense region

```python
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

# Generate crescent-shaped data (K-Means fails here)
X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# DBSCAN
db = DBSCAN(eps=0.2, min_samples=5)
labels = db.fit_predict(X_moons)

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Clusters found: {n_clusters}")
print(f"Noise points: {n_noise}")

plt.scatter(X_moons[:, 0], X_moons[:, 1], c=labels, cmap='viridis', s=30)
plt.title('DBSCAN Clustering')
plt.show()
```

---

## Hierarchical Clustering

Builds a tree of clusters by either merging (agglomerative) or splitting (divisive).

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Agglomerative clustering
agg = AgglomerativeClustering(n_clusters=4)
labels = agg.fit_predict(X)

# Dendrogram
linked = linkage(X[:50], method='ward')
dendrogram(linked)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()
```

---

## Principal Component Analysis (PCA)

PCA is the most popular **dimensionality reduction** technique. It finds new axes
(principal components) that capture the maximum variance in the data.

### Why Reduce Dimensions?

- **Visualization**: Plot high-dimensional data in 2D or 3D
- **Speed**: Fewer features means faster training
- **Noise reduction**: Remove components that mostly capture noise
- **Multicollinearity**: Remove correlated features
- **The Curse of Dimensionality**: Many algorithms degrade with too many features

### How PCA Works

1. Center the data (subtract the mean).
2. Compute the covariance matrix.
3. Find the eigenvectors (directions) and eigenvalues (importance) of the covariance matrix.
4. Sort eigenvectors by eigenvalue (descending).
5. Project the data onto the top K eigenvectors.

### Implementation

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load and scale data
iris = load_iris()
X = StandardScaler().fit_transform(iris.data)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Explained variance
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance captured:", sum(pca.explained_variance_ratio_))

# Visualize
plt.figure(figsize=(8, 6))
for i, name in enumerate(iris.target_names):
    mask = iris.target == i
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], label=name, s=40)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
plt.title('Iris Dataset - PCA')
plt.legend()
plt.show()
```

### Choosing the Number of Components

```python
pca_full = PCA()
pca_full.fit(X)

cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)

plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, 'bo-')
plt.axhline(y=0.95, color='r', linestyle='--', label='95% threshold')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('PCA - Scree Plot')
plt.legend()
plt.show()

# Choose components that capture 95% of variance
pca_95 = PCA(n_components=0.95)
X_reduced = pca_95.fit_transform(X)
print(f"Components needed for 95% variance: {pca_95.n_components_}")
```

### PCA for Speeding Up ML

```python
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import time

digits = load_digits()
X_digits = StandardScaler().fit_transform(digits.data)

# Without PCA (64 features)
start = time.time()
scores = cross_val_score(RandomForestClassifier(n_estimators=50, random_state=42),
                         X_digits, digits.target, cv=5)
print(f"Without PCA: {scores.mean():.4f} in {time.time()-start:.2f}s")

# With PCA (reduce to 20 components)
pca = PCA(n_components=20)
X_pca = pca.fit_transform(X_digits)

start = time.time()
scores = cross_val_score(RandomForestClassifier(n_estimators=50, random_state=42),
                         X_pca, digits.target, cv=5)
print(f"With PCA:    {scores.mean():.4f} in {time.time()-start:.2f}s")
```

---

## t-SNE for Visualization

t-SNE is another dimensionality reduction technique, specifically designed for
**visualization** of high-dimensional data.

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_digits)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=digits.target, cmap='tab10', s=10)
plt.colorbar(scatter, label='Digit')
plt.title('t-SNE Visualization of Digits Dataset')
plt.show()
```

**PCA vs t-SNE:**
- PCA preserves global structure, is fast and deterministic
- t-SNE preserves local structure, is slow and non-deterministic
- Use PCA for preprocessing, t-SNE for visualization only

---

## Practical Pipeline: Clustering with Preprocessing

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('kmeans', KMeans(n_clusters=3, random_state=42, n_init=10))
])

labels = pipeline.fit_predict(iris.data)
print(f"Cluster assignments: {np.bincount(labels)}")
```

---

## Key Takeaways

1. K-Means is simple and fast but requires specifying K and assumes spherical clusters.
2. Use the Elbow Method and Silhouette Score to choose K.
3. DBSCAN finds arbitrary-shaped clusters and identifies outliers as noise.
4. PCA reduces dimensionality by projecting data onto directions of maximum variance.
5. Choose enough components to capture 95% or more of the variance.
6. t-SNE is excellent for visualizing high-dimensional data but not for preprocessing.
7. Always scale data before applying distance-based algorithms (K-Means, PCA, DBSCAN).
