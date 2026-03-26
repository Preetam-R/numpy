import numpy as np

data = np.array([10, 12, 11, 13, 9, 100, 10, 12, -50, 11])

mean = data.mean()
std  = data.std()

# Boolean mask for outliers
outliers = np.abs(data - mean) > 2 * std

# Replace outliers with the mean
cleaned = np.where(outliers, mean, data)

print("Original :", data)
print("Outliers  :", data[outliers])
print("Cleaned  :", cleaned)