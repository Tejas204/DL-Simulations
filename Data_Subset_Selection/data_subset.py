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
    
    def __getlength__(self, timestamps):
        """
        Return the length of given timestamps
        
        :param self: DesClass specific parameterscription
        :param timestamps: Array like object
        """
        return np.size(timestamps)

    
    def remove_time_stamps(self, start, end):
        """
        Remove data at timestamps from start index to end index.
        Return both subsets
        
        :param self: Class specific parameters
        :param start: start index of removal
        :param end: end index of removal
        """
        removed_timestamps = self.timestamps[start: end+1]

        if start == 0:
            selected_timestamps = self.timestamps[end+1: ]
        else:
            selected_timestamps = np.append(self.timestamps[: start], self.timestamps[end+1: ])

        return selected_timestamps, removed_timestamps
    
    def write_data(self, subset, file_name):
        """
        Write data to a text file for later use
        
        :param self: Class specific parameters
        :param subset: data to be written to the file
        :param file_name: file name of the data file
        """
        with open(str(file_name)+".txt", "w+") as file:
            file.write(str(subset))
            file.close()

subset = DataSubset()
remaining, removed = subset.remove_time_stamps(2, 10)
subset.write_data(remaining, "data_subset")

