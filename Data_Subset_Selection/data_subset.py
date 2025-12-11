# Imports
import numpy as np
import matplotlib.pyplot as plt

# Create Class for subset selection
class DataSubset():
    """
    Class: DataSubset
    Used to select a subset from a given dataset
    """

    def __init__(self):
        """
        Initialize the class DataSubset
        
        :param self: Defines constants
        """
        self.timestamps = np.array([i for i in range(100)])

    def __getitem__(self, index):
        """
        Return data at specific timestamp
        
        :param self: Class specific parameters
        :param index: to fetch the timestamp at given index
        """
        return self.timestamps[index]
    
    def remove_time_stamps(self, start, end):
        """
        Remove data at timestamps from start index to end index.
        Return both subsets
        
        :param self: Class specific parameters
        :param start: start index of removal
        :param end: end index of removal
        """
        removed_timestamps = self.timestamps[start: end]

        if start == 0:
            selected_timestamps = self.timestamps[end: ]
        else:
            selected_timestamps = np.append(self.timestamps[: start], self.timestamps[end: ])

        return selected_timestamps, removed_timestamps


subset = DataSubset()

