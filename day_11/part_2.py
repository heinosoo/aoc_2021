import numpy as np

def step(OP):
    flashes = np.zeros(OP.shape, bool)
    OP += 1
    while np.any(OP > 9):
        for x, y in zip(*np.where(OP > 9)):
            if not flashes[x, y]:
                OP[max(x-1, 0):x+2, max(y-1, 0):y+2] += 1
                OP[x, y] = -10
                flashes[x, y] = True
    OP[flashes] = 0
    return np.all(flashes)

with open('input.txt') as f:
    OP = np.array([[int(n) for n in list(line.strip())] for line in f.readlines()])

for i in range(1, 1000):
    if step(OP):
        print(i)
        break
