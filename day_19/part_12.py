import numpy as np
from collections import defaultdict


class Map:
    def __init__(self, scans):
        self.M = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
        for x, y, z in scans[0]:
            self.M[x][y][z] = True
        self.scanners = [(0, 0, 0)]
        self.update_beacons()
        self.extend(scans[1:])

    def update_beacons(self):
        self.beacons = [(x, y, z) for x, Y in self.M.items() for y, Z in Y.items()
                        for z, n in Z.items() if n]
        print('Scanners:', len(self.scanners))
        print('Beacons:', len(self.beacons))

    def add(self, scan):  # Terribly inefficient..
        for scan_p in self.scanner_perms(scan):
            for x1, y1, z1 in scan_p:
                for x2, y2, z2 in self.beacons:
                    dx, dy, dz = x2-x1, y2-y1, z2-z1
                    if sum([self.M[x+dx][y+dy][z+dz] for x, y, z in scan_p]) >= 12:
                        for x, y, z in scan_p:
                            self.M[x+dx][y+dy][z+dz] = True
                        self.scanners.append((dx, dy, dz))
                        self.update_beacons()
                        return True
        return False

    def extend(self, scans):
        if not scans:
            return True
        for i in range(len(scans)):
            if self.add(scans[i]):
                return self.extend(scans[:i]+scans[i+1:])
        print("Couldn't build map. Scanners left:", len(scans))
        return False

    def scanner_perms(self, scan):
        S = [[[x, y, z], [x, -y, -z], [-x, y, -z], [-x, -y, z],
              [y, z, x], [y, -z, -x], [-y, z, -x], [-y, -z, x],
              [z, x, y], [z, -x, -y], [-z, x, -y], [-z, -x, y],
              [-x, -z, -y], [-x, z, y], [x, -z, y], [x, z, -y],
              [-y, -x, -z], [-y, x, z], [y, -x, z], [y, x, -z],
              [-z, -y, -x], [-z, y, x], [z, -y, x], [z, y, -x]]
             for x, y, z in scan]
        return np.transpose(S, axes=(1, 0, 2))


with open('input.txt') as f:
    S = f.read().strip().split('\n\n')
    S = [[[int(c) for c in beacon.split(',')]
         for beacon in scan.split('\n')[1:]] for scan in S]

M = Map(S)
print(len(M.beacons))
print(max([abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
           for x1, y1, z1 in M.scanners for x2, y2, z2 in M.scanners]))
