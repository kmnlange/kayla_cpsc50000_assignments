import numpy as np

x = np.array([2.0,1.8,1.5,1.2,1.0,0.8,0.5,0.2])
y = np.array([19,21,30,54,61,82,83,102])

print("X mean, Y mean:")
print(x.mean(), y.mean())
print("X stdev, Y stdev")
print(x.std(ddof=1), y.std(ddof=1))
print("Sample Covariance Matrix:")
print(np.cov(x, y))
print("Correlation Matrix:")
print(np.corrcoef(x, y))