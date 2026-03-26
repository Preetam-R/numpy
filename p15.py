import numpy as np

np.random.seed(42)
data = np.random.randint(10, 100, size=8)

# Min-Max normalization
normalized = (data - data.min()) / (data.max() - data.min())

print("Original :", data)
print("Normalized:", np.round(normalized, 2))