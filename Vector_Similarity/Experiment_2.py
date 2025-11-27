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