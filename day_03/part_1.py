import numpy as np

a = [[int(i) for i in line] for line in np.loadtxt("input.txt", 'U')]
b = (np.array(a).sum(axis=0))//(len(a)//2)
gamma = int(''.join(map(str, b)), base=2)
epsilon = 2**len(a[0])-1-gamma

print(gamma*epsilon)
