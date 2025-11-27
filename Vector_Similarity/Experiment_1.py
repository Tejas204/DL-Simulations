# Imports
import numpy as np
import matplotlib.pyplot as plt
import torch
from mpl_toolkits.mplot3d import Axes3D

# Hyperparameters
n_top_features = 5
scoring_threshold = 0.5

print(f"\n----------------------------- Features -----------------------------\n")

# Generate top n feature vectors based on score function
# Assume that the feature vectors are already selected based on the score function.
feature_matrix = np.random.rand(5, 3)
scores = np.sort(np.random.rand(5), axis=None)[::-1]
print(f"Feature matrix: \n{feature_matrix}\n")
print(f"Scores: \n{scores}")


# -------------------------------------------------------------------------------------------------
# Experiment 1:
# The score function returns the top features that activate for a concept
# We sort the score function in descending order
# Thus, the most important feature is at the top
# Compute the similarity score and subtract from the actual score
# -------------------------------------------------------------------------------------------------
print(f"\n----------------------------- Experiment 1 -----------------------------\n")
def similarity_scoring(x, y):
    score = np.inner(x, y)
    return score

scores_wrt_top = []
for i in range(0, n_top_features):
    if i == 0:
        scores_wrt_top.append(0)
    else:
        scores_wrt_top.append(similarity_scoring(feature_matrix[0], feature_matrix[i]))

print(f"Scores with respect to the first feature are:\n{scores_wrt_top}\n")

# Update scores
updated_scores = np.subtract(scores, np.array(scores_wrt_top))

print(f"Updated scores with respect to the first feature are:\n{updated_scores}\n")

# Drop scores
for i in range(len(updated_scores)):
    if updated_scores[i] >= scoring_threshold:
        continue
    else:
        updated_scores[i] = 0


print(f"Updated scores after thresholding are:\n{updated_scores}\n")

# Filter out the feature that is not zero
filtered_feature_matrix = np.random.rand(5, 3)
filtered_indices = []
for i in range(len(updated_scores)):
    if updated_scores[i] > 0:
        filtered_feature_matrix[i] = feature_matrix[i]
    else:
        filtered_feature_matrix[i] = 0

print(f"Filtered feature matrix: \n{filtered_feature_matrix}\n")

# -------------------------------------------------------------------------------------------------
# PLOT 1: Feature matrix in 3D with arrows
# -------------------------------------------------------------------------------------------------
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')

for i in range(5):
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

for i in range(5):
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