import numpy as np
import regex as re

with open('input.txt') as f:
    R = re.compile(r'^(\S+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    steps = [(R.match(line)[1] == 'on', [int(n) for n in R.match(line)[2:]])
             for line in f.readlines()]

C = 50  # Test for part 2 would require 13 PiB. :p
reactor = np.zeros((2*C+1,)*3, bool)
for state, (x1, x2, y1, y2, z1, z2) in steps:
    reactor[x1+C:x2+C+1, y1+C:y2+C+1, z1+C:z2+C+1] = state

print(np.count_nonzero(reactor))
