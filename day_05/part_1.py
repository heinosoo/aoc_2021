import numpy as np

lines = []
for d, _, b in np.loadtxt('input.txt', 'U'):
    d = [int(n) for n in d.split(',')]
    b = [int(n) for n in b.split(',')]
    lines.append([d, b])

smoke = np.zeros((np.max(lines)+1,)*2, int)
for d, b in lines:
    if d[0] == b[0] or d[1] == b[1]:
        x1, x2, y1, y2 = *sorted([d[0], b[0]]), *sorted([d[1], b[1]])
        smoke[x1:x2+1, y1:y2+1] += 1

print(np.count_nonzero(smoke > 1))
