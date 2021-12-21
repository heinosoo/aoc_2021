import numpy as np

dice_rolls = [i+j+k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)]
dice_counts = [dice_rolls.count(roll) for roll in range(10)]

with open('input.txt') as f:
    pos = [int(line[-2]) for line in f.readlines()]

state = np.zeros((10, 22, 10, 22), int)
state[pos[0]-1, 0, pos[1]-1, 0] = 1
wins = [0, 0]

for i in range(200):
    new_state = np.zeros((10, 22, 10, 22), int)
    for p1, s1, p2, s2 in np.transpose(np.nonzero(state)):
        n = state[p1, s1, p2, s2]
        for roll, m in enumerate(dice_counts):
            new_pos = (p1+roll) % 10
            new_score = min(new_pos + s1 + 1, 21)
            new_state[new_pos, new_score, p2, s2] += m*n
    wins[i % 2] += np.sum(new_state[:, -1, :, :])
    new_state[:, -1, :, :] = 0
    state = new_state.transpose(2, 3, 0, 1)  # Exchange players 1 and 2
    if not np.count_nonzero(state):
        print(max(wins))
        break
