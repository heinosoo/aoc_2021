import numpy as np

with open('input.txt') as f:
    M = [[int(n) for n in list(line.strip())] for line in f.readlines()]

Mp = (np.pad(M, 1, 'constant', constant_values=10))
Mp_a, Mp_b, Mp_c, Mp_d = np.roll(Mp, 1, 0), np.roll(Mp, -1, 0), np.roll(Mp, 1, 1), np.roll(Mp, -1, 1)
Mp_low = (Mp < Mp_a) & (Mp < Mp_b) & (Mp < Mp_c) & (Mp < Mp_d)
print((Mp[np.where(Mp_low)]+1).sum())
