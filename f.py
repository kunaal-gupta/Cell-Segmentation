import numpy as np

# Create a sample 3D array with shape (2, 2, 2)
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Collapse the array along the z-axis (axis=2) into a 2D array
arr_2d = np.sum(arr_3d, axis=1)

# Print the original and collapsed arrays
print("Original 3D array:\n", arr_3d)
print("Collapsed 2D array:\n", arr_2d)