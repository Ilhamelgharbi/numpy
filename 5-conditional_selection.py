import numpy as np
tab = np.array([36.5, 37.0, 38.2, 39.1, 40.0])
v = float(input("Enter a temperature to check: "))
indice = np.where(tab > v)
print (f"Temperatures above {v}°C are : {tab[indice]}")