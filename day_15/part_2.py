import numpy as np

with open('input.txt') as f:
    risk = np.array([[int(n) for n in list(line.strip())] for line in f.readlines()])
    risk = np.hstack((risk, risk+1, risk+2, risk+3, risk+4))  # extend horizontally
    risk = np.vstack((risk, risk+1, risk+2, risk+3, risk+4))  # extend vertically
    risk = np.vectorize(lambda x: (x-1) % 9 + 1)(risk)        # wrap risk values
    X, Y = risk.shape
    risk_path = np.zeros(risk.shape, int)
    edge = [(0, 0)]

while edge:
    x, y = edge.pop(risk_path[tuple(zip(*edge))].argmin())
    r = risk_path[x, y]
    points = (x, y-1), (x, y+1), (x-1, y), (x+1, y)
    for x, y in points:
        if x >= 0 and y >= 0 and x < X and y < Y and not risk_path[x, y]:
            risk_path[x, y] = r + risk[x, y]
            edge.append((x, y))

print(risk_path[-1, -1])
