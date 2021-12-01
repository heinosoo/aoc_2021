import numpy as np

d = np.loadtxt("input.txt", int)
d = [d[i]+d[i+1]+d[i+2] for i in range(len(d)-2)]
print(len([i for i in range(len(d)-1) if d[i+1]-d[i] > 0]))
