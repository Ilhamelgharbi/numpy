
import numpy as np


tab  = np.array([36.5, 37.0, 38.2, 39.1, 40.0])

tab_norm = (tab - np.mean(tab)) / np.std(tab)
print("Normalized temperatures:", tab_norm)
temp = tab_norm
temp1 = np.mean(temp)
temp2 = np.std(temp) 
temp3 = np.median(temp)
print("Mean temperature:", temp1)
print("Standard deviation of temperature:", temp2)
print("Median temperature:", temp3)