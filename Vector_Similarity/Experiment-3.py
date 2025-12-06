import torch
import numpy as np
import matplotlib.pyplot as plt

# Define input vector and matrix
x = np.array([[1, 2, 3]])
print(f"X:\n{x}\n")

W = np.array([[1, 2, 3, 1, 0], [0, 1, 0, 1, 1], [1, 2, 1, 0, 3]], np.int32)
print(f"W:\n{W}\n")

# Project x into the space of W
y = np.dot(x, W)
print(f"Y:\n{y}")

# Visualize x and y
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')

for i in range(1):
    x, y, z = x[i]
    c = colors[i % len(colors)]

    ax1.scatter(x, y, z, color=c, s=60)
    ax1.quiver(0, 0, 0, x, y, z, color=c, arrow_length_ratio=0.1)

ax1.set_title("Input (3D)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
plt.show()