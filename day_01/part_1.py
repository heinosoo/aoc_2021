import numpy as np

d = np.loadtxt("input.txt", int)
print(len([i for i in range(len(d)-1) if d[i+1]-d[i] > 0]))
