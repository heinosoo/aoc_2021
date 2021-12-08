def decode(test):
    A = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for n in test.split(' '):
        A[len(n)].append(set(n))

    # Known numbers
    n1 = A[2][0]
    n4 = A[4][0]
    n7 = A[3][0]
    n8 = A[7][0]

    # Brute forcing the segments by elimination
    abfg = set.intersection(*A[6])
    adg = set.intersection(*A[5])
    cf = n1
    bd = n4 - n1
    a = n7 - n1
    b = bd - adg
    d = bd - b
    g = adg - a - d
    f = abfg - a - b - g
    c = cf - f
    e = n8 - a - b - c - d - f - g

    M = [a | b | c | e | f | g,
         n1,
         a | c | d | e | g,
         a | c | d | f | g,
         n4,
         a | b | d | f | g,
         a | b | d | e | f | g,
         n7,
         n8,
         a | b | c | d | f | g]
    return {''.join(sorted(M[n])): n for n in range(10)}


with open('input.txt') as f:
    L = [line.strip().split(' | ') for line in f.readlines()]

c = 0
for test, N in L:
    D = decode(test)
    N = [''.join(sorted(n)) for n in N.split(' ')]
    c += 1000*D[N[0]]+100*D[N[1]]+10*D[N[2]]+D[N[3]]

print(c)
