from collections import defaultdict

with open('input.txt') as f:
    template = f.readline().strip()
    rules = [rule.strip().split(' -> ') for rule in f.readlines()[1:]]
    rules = {pair: [pair[0]+ins, ins+pair[1]] for pair, ins in rules}

# Going to keep track of the number of pairs only.
polymer = defaultdict(lambda: 0)
for i in range(len(template)-1):
    polymer[template[i:i+2]] += 1
for _ in range(40):
    new_polymer = polymer.copy()
    for pair, (a, b) in rules.items():
        if pair in polymer:
            new_polymer[a] += polymer[pair]
            new_polymer[b] += polymer[pair]
            new_polymer[pair] -= polymer[pair]
    polymer = new_polymer

# Double counting because of pairs, first and last don't change
elements = defaultdict(lambda: 0)
elements[template[0]] = elements[template[-1]] = 1
for (a, b), n in polymer.items():
    elements[a] += n
    elements[b] += n
result = (max(elements.values()) - min(elements.values()))//2

print(result)
