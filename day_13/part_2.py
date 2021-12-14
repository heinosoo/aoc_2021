import numpy as np

D = np.loadtxt('input.txt', int, delimiter=',', comments='fold')
F = np.loadtxt('input.txt', [('f0', 'U12'), ('f1', int)], delimiter='=', skiprows=len(D))

for fold, n in F:
    if fold[-1] == 'y':
        D = [[X, 2*n-Y] if Y > n else [X, Y] for X, Y in D]
    else:
        D = [[2*n-X, Y] if X > n else [X, Y] for X, Y in D]

A = np.transpose(D)
X = np.full((max(A[0]+1), max(A[1]+1)), ' ')
X[A[0], A[1]] = '#'
for a in X.transpose():
    print(''.join(a))
