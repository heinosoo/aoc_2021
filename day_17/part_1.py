import numpy as np


def probe_hit(vx, vy):
    x = y = 0
    while vy > 0 or y > Y1:
        x += vx
        y += vy
        vy -= 1
        if vx:
            vx -= vx//abs(vx)
        if X1 <= x <= X2 and Y1 <= y <= Y2:
            return True
    return False


T = np.fromregex('input.txt', r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', int)
(X1, X2), (Y1, Y2) = sorted(T[0][:2]), sorted(T[0][2:])
vx_min = int(np.sign(X1)*np.ceil((np.sqrt(8*abs(X1)+1)-1)/2))   # vx becomes zero before target.
vx_max = int(np.sign(X2)*np.floor((np.sqrt(8*abs(X2)+1)-1)/2))  # vx becomes zero after target.
vy_min = Y1-1  # Would undershoot on first turn already.
vy_max = 200  # High enough to get the right answer. :p

vy_top = vy_min
for vy in range(vy_min, vy_max+1):
    for vx in range(vx_min, vx_max+1):
        if probe_hit(vx, vy):
            vy_top = max(vy_top, vy)

print(vy_top*(vy_top+1)//2)
