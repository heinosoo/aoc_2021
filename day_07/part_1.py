import numpy as np

crabs = np.loadtxt('input.txt', int, delimiter=',')
print(abs(crabs - round(np.median(crabs))).sum())
