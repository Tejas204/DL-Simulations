# Imports
import numpy as np
import matplotlib.pyplot as plt

# Create Class for subset selection
class DataSubset():
    def __init__(self):
        self.timestamps = np.array([i for i in range(100)])

    def __getitem__(self, index):
        return self.timestamps[index]
    
    def remove_time_stamps(self, start, end):
        pass

# Create a random number array and sort it
# Reason: Timestamps go from 0 to 100 --> Ascending order
# print(f"Timestamps are: {timestamps}")