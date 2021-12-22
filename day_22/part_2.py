import numpy as np
import regex as re

with open('input.txt') as f:
    R = re.compile(r'^(\S+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    steps = [(R.match(line)[1] == 'on', [int(n) for n in R.match(line)[2:]])
             for line in f.readlines()]

# Split the grid by corners.
X = [x1 for _, (x1, _, _, _, _, _) in steps] + [x2+1 for _, (_, x2, _, _, _, _) in steps]
Y = [y1 for _, (_, _, y1, _, _, _) in steps] + [y2+1 for _, (_, _, _, y2, _, _) in steps]
Z = [z1 for _, (_, _, _, _, z1, _) in steps] + [z2+1 for _, (_, _, _, _, _, z2) in steps]
X = sorted(np.unique(X))
Y = sorted(np.unique(Y))
Z = sorted(np.unique(Z))

reactor = np.zeros((len(X)-1, len(Y)-1, len(Z)-1), int)
for state, (x1, x2, y1, y2, z1, z2) in steps:
    xi1, xi2 = X.index(x1), X.index(x2+1)
    yi1, yi2 = Y.index(y1), Y.index(y2+1)
    zi1, zi2 = Z.index(z1), Z.index(z2+1)
    reactor[xi1:xi2, yi1:yi2, zi1:zi2] = state

# Add a measure to the grid.
Xs = np.array(X[1:])-(X[:-1])
Ys = np.array(Y[1:])-(Y[:-1])
Zs = np.array(Z[1:])-(Z[:-1])

# Add up the volume of all active sub-blocks.
print(sum((Xs[x]*Ys[y]*Zs[z] for x, y, z in zip(*np.where(reactor)))))
