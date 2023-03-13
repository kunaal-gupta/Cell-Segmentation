import numpy as np

# Create a 3D numpy array of shape (3, 4, 5)
a = np.arange(60).reshape((3, 4, 5))

# Slice along the first dimension, taking the first two "pages" of the array
b = a[0:2, :, :]

# Slice along the second dimension, taking the second and third "columns" of the array
c = a[:, 1:3, :]

# Slice along the third dimension, taking every other "slice" of the array
d = a[:, :, 1]

# Print the original and sliced arrays
print("Original array:\n", a)
print("Sliced array (first dimension):\n", b)
print("Sliced array (second dimension):\n", c)
print("Sliced array (third dimension):\n", d)