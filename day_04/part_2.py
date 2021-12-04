import numpy as np

with open('input.txt') as f:
    Ns = [int(n) for n in f.readline().split(',')]

B = np.loadtxt('input.txt', skiprows=2, dtype=int)
Bn = len(B)//len(B[0])  # Number of bingo tables
B = B.reshape(Bn, 5, 5)  # 3d array

M = np.ones((Bn, 5, 5), int)  # Hit mask
BM = np.ones(Bn, int)  # Bingo mask
H = np.zeros((Bn, 5), int)  # Horizontal hit count
V = np.zeros((Bn, 5), int)  # Vertical hit count

for N in Ns:  # Assuming no duplicates here..
    for z, y, x in np.argwhere(B == N):
        M[z, y, x] = 0
        H[z, y] += 1
        V[z, x] += 1
        if H[z, y] == 5 or V[z, x] == 5:
            BM[z] = 0
            if not BM.sum():
                print('Last bingo!')
                print((M[z]*B[z]).sum()*N)
                break
    else:
        continue
    break
