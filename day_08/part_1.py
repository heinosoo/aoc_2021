with open('input.txt') as f:
    L = [line.strip().split(' | ') for line in f.readlines()]

c = 0
for _, N in L:
    for n in N.split(' '):
        if len(n) in [2, 3, 4, 7]:
            c += 1
print(c)
