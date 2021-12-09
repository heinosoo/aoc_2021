import numpy as np
from scipy.ndimage import label

with open('input.txt') as f:
    M = [[int(n) for n in list(line.strip())] for line in f.readlines()]

M_labels = label(np.where(np.array(M) < 9, 1, 0))
sizes = [np.count_nonzero(M_labels[0] == n) for n in range(1, M_labels[1]+1)]
print(np.prod(sorted(sizes)[-3:]))
