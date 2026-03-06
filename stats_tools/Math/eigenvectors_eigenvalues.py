import numpy as np

# Dataset
height = np.array([2.0,1.8,1.5,1.2,1.0,0.8,0.5,0.2])
weight = np.array([19,21,30,54,61,82,83,102])

# Step 1: Standardize (z-scores)
height_z = (height - height.mean()) / height.std(ddof=1)
weight_z = (weight - weight.mean()) / weight.std(ddof=1)

# Stack into a 2xN matrix
Z = np.vstack((height_z, weight_z))  # shape 2 x N

# Step 2: Covariance matrix of standardized data
cov_matrix = np.cov(Z)

print("Covariance matrix:")
print(cov_matrix)

# Step 3: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors (columns correspond to eigenvectors):")
print(eigenvectors)

idx = np.argmax(eigenvalues)
pc1_vector = eigenvectors[:, idx]

# Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Scale eigenvectors to get simple form
v1 = eigenvectors[:, np.argmax(eigenvalues)]
v1_scaled = v1 / v1[0]  # first entry = 1

v2 = eigenvectors[:, np.argmin(eigenvalues)]
v2_scaled = v2 / v2[0]

print("Principal Component 1 (PC1):", v1_scaled)
print("Principal Component 2 (PC2):", v2_scaled)

# Step 4: Compute explained variance
explained_variance_ratio = eigenvalues / eigenvalues.sum()
print("\nExplained variance ratio:")
for i, ratio in enumerate(explained_variance_ratio):
    print(f"Principal Component {i+1}: {ratio*100:.1f}% of variance")

print("\nInterpretation:")
print("Principal Component 1 (corresponding to the first eigenvalue) carries "
      f"{explained_variance_ratio[0]*100:.1f}% of the variance of the data, "
      f"while Principal Component 2 carries {explained_variance_ratio[1]*100:.1f}% of the variance.")
