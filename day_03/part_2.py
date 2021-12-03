import numpy as np

a = np.array([[int(i) for i in line] for line in np.loadtxt("input.txt", 'U')])

def filter(a, co2=0, i=0):
    if len(a) < 2:
        return int(''.join(map(str, a[0])), base=2)
    c = a[:, i].sum()//((len(a)+1)//2)  # +1 after //2 to get 0 for equal case.
    new_a = [n for n in a if n[i] == abs(c-co2)]
    return filter(np.array(new_a), co2, i+1)

filter(a)*filter(a, co2=1)
