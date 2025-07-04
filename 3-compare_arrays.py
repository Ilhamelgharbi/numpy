import numpy as np

tab1 = np.array([36.5, 37.0, 38.2, 39.1, 40.0])
tab2 = np.array([36.5, 37.0, 38.0, 39.0, 40.0])
dif = np.where(tab1 != tab2)
for i in dif[0]:
    print(f"Difference at index {i}: {tab1[i]} vs {tab2[i]}")