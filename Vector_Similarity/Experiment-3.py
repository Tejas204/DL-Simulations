import torch
import numpy as np
import matplotlib.pyplot as plt

# Define input vector and matrix
input = np.array([[1, 2, 3]])
print(f"X:\n{input}\n")

W = np.array([[1, 2, 3], [0, 1, 0], [1, 2, 1]], np.int32)
print(f"W:\n{W}\n")

# Project x into the space of W
output = np.dot(input, W)
print(f"Y:\n{output}")

# Visualize x and y
input_output = [input, output]
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')

for i in range(2):
    x, y, z = input_output[i][0]
    c = colors[i % len(colors)]

    ax1.scatter(x, y, z, color=c, s=60)
    ax1.quiver(0, 0, 0, x, y, z, color=c, arrow_length_ratio=0.1)
    ax1.text(x, y, z, "Input" if i == 0 else "Output", color=c )

ax1.set_title("Input (3D)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
plt.show()