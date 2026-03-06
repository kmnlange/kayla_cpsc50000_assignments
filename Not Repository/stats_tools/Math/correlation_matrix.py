import numpy as np
height = np.array([2.0,1.8,1.5,1.2,1.0,0.8,0.5,0.2])
weight = np.array([19,21,30,54,61,82,83,102])

print("Correlation Matrix:")
print(np.corrcoef(height, weight))