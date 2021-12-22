energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
goal = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
rooms = [2, 4, 6, 8]
N = 2

def moves(M):
    r = []
    blocked = [i for i, n in enumerate(M) if len(n) != 0 and i not in rooms]
    for i, a in enumerate(M):
        if not a or all([goal[n] == i for n in M[i]]):
            continue
        g = goal[a[-1]]
        if i not in rooms:
            u, p = sorted([i, g])
            if (all([j not in blocked for j in range(u+1, p)]) and
               all([goal[n] == g for n in M[g]])):
                return [(i, g, cost(M, i, g))]
        else:
            lower = max([-1] + [j for j in blocked if j < i])
            upper = min([11] + [j for j in blocked if j > i])
            options = [(i, j, cost(M, i, j)) for j in
                       list(range(lower+1, i))+list(range(i+1, upper))
                       if j not in rooms]
            r.extend(options)
    return r

def cost(M, i, j):
    if i in rooms:
        return energy[M[i][-1]]*(abs(i-j) + 1 + N - len(M[i]))
    else:
        return energy[M[i][-1]]*(abs(i-j) + N - len(M[j]))

def solve(M, C=0):
    if C > 20000:
        return C
    if all([goal[n] == i for i in range(11) for n in M[i]]):
        return C
    res = 100000
    for i, j, c in moves(M):
        M[j].append(M[i].pop())
        res = min(solve(M, C+c), res)
        M[i].append(M[j].pop())
    return res

with open('input.txt') as f:
    _, _, K, L = (f.readline() for _ in range(4))
    M0 = [[], [], [L[3], K[3]], [], [L[5], K[5]], [],
          [L[7], K[7]], [], [L[9], K[9]], [], []]

print(solve(M0))
