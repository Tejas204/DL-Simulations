# Imports
import numpy as np
import matplotlib.pyplot as plt
import torch
from mpl_toolkits.mplot3d import Axes3D

# Hyperparameters
n_top_features = 10
scoring_threshold = 0.5

print(f"\n----------------------------- Experiment 2 -----------------------------\n")

# Generate top n feature vectors based on score function
# Assume that the feature vectors are already selected based on the score function.
feature_matrix = np.random.rand(n_top_features, 3)
scores = np.sort(np.random.rand(n_top_features), axis=None)
print(f"Feature matrix: \n{feature_matrix}\n")
print(f"Scores: \n{scores}")

# -------------------------------------------------------------------------------------------------
# Experiment 2:
# The score function returns the top features that activate for a concept
# We calculate the similarity matrix
# Then update the scores by subtracting average similarity for each feature
# Then threshold the featrues by average updated score
# -------------------------------------------------------------------------------------------------

# Compute similarity matrix
similarity_matrix = np.inner(feature_matrix, feature_matrix)

# Compute updates scores
updated_scores = []
for i in range(n_top_features):
    updated_scores.append(scores[i] - np.sum(similarity_matrix[i]) + similarity_matrix[i][i])
updated_scores = np.array(updated_scores)

print(f"Similarity matrix:\n {similarity_matrix}")
print(f"\nUpdates scores:\n {updated_scores}")
print(f"\nAverage score: {np.average(updated_scores)}")

# Threshold the scores on average updated score
for i in range(len(updated_scores)):
    if updated_scores[i] >= np.average(updated_scores):
        continue
    else:
        updated_scores[i] = 0

# Create final feature matrix
filtered_feature_matrix = np.random.rand(n_top_features, 3)
for i in range(len(updated_scores)):
    if updated_scores[i] != 0:
        filtered_feature_matrix[i] = feature_matrix[i]
    else:
        filtered_feature_matrix[i] = 0

print(f"\nUpdated scores after thresholding are:\n{updated_scores}\n")
print(f"\nFiltered feature matrix: \n{filtered_feature_matrix}\n")

# -------------------------------------------------------------------------------------------------
# PLOT 1: Feature matrix in 3D with arrows
# -------------------------------------------------------------------------------------------------
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')

for i in range(n_top_features):
    x, y, z = feature_matrix[i]
    c = colors[i % len(colors)]

    ax1.scatter(x, y, z, color=c, s=60)
    ax1.quiver(0, 0, 0, x, y, z, color=c, arrow_length_ratio=0.1)
    ax1.text(x, y, z, f"{scores[i]}", color=c)

ax1.set_title("Feature Matrix (3D)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, projection='3d')

for i in range(n_top_features):
    x, y, z = filtered_feature_matrix[i]
    c = colors[i % len(colors)]

    ax2.scatter(x, y, z, color=c, s=60)
    ax2.quiver(0, 0, 0, x, y, z, color=c, arrow_length_ratio=0.1)
    ax2.text(x, y, z, f"{scores[i]}", color=c)

ax2.set_title("Filtered Feature Matrix (3D)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
plt.show()

