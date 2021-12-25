import numpy as np

def step():
    move_e = [(x, y) for x, y in zip(*np.where(Me)) if not Me[x, y-1] and not Ms[x, y-1]]
    if move_e:
        new_e = [(x, y-1) for x, y in move_e]
        Me[tuple(zip(*move_e))] = False
        Me[tuple(zip(*new_e))] = True
    move_s = [(x, y) for x, y in zip(*np.where(Ms)) if not Me[x-1, y] and not Ms[x-1, y]]
    if move_s:
        new_s = [(x-1, y) for x, y in move_s]
        Ms[tuple(zip(*move_s))] = False
        Ms[tuple(zip(*new_s))] = True
    return (len(move_e)+len(move_s))

with open('input.txt') as f:  # The directions are reversed, so they move backwards.
    M = f.read().strip().split('\n')
    Me = np.flip(np.array([[sc == '>' for sc in line] for line in M]))
    Ms = np.flip(np.array([[sc == 'v' for sc in line] for line in M]))

N = 1
while step():
    N += 1
print(N)
