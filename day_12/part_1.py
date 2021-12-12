with open('input.txt') as f:
    caves = {}
    for line in f.readlines():
        a, b = line.strip().split('-')
        if a not in caves:
            caves[a] = set()
        if b not in caves:
            caves[b] = set()
        caves[a].add(b)
        caves[b].add(a)
    caves_big = {cave for cave in caves if str.isupper(cave)}


def paths(cave='start', caves_visited=['start']):
    P = []
    for new_cave in caves[cave]:
        if new_cave not in caves_visited or new_cave in caves_big:
            caves_visited.append(new_cave)
            P += [[cave] + p for p in paths(new_cave, caves_visited) if p]
            caves_visited.pop()
    if cave == 'end':
        return [['end']]
    return P


len(paths())
