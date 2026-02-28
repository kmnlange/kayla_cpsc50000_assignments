import numpy as np

height = np.array([2.0,1.8,1.5,1.2,1.0,0.8,0.5,0.2])
weight = np.array([19,21,30,54,61,82,83,102])

# Compute z-scores
height_z = (height - height.mean()) / height.std(ddof=1)
weight_z = (weight - weight.mean()) / weight.std(ddof=1)

print("\nZ-scores for height:")
print(height_z)
print("Z-scores for weight:")
print(weight_z)

print("\nCovariance Matrix of Z-scores:")
print(np.cov(height_z, weight_z))

print("\nCorrelation Matrix:")
print(np.corrcoef(height_z, weight_z))