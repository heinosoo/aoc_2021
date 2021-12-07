import numpy as np

crabs = np.loadtxt('input.txt', int, delimiter=',')
N = int(round(np.average(crabs)))  # Some error in this method it seems, but close.
D = min([sum([a*(a+1)//2 for a in abs(crabs - n)]) for n in [N-1, N, N+1]])
print(N, D)
