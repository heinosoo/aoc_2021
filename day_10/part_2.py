open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_chart = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
with open('input.txt') as f:
    for line in f.readlines():
        open_chunks = []
        corrupt = False
        for c in line.strip():
            if c in open_close:
                open_chunks.append(c)
            else:
                if open_close[open_chunks.pop()] != c:
                    corrupt = True
                    break
        if not corrupt:
            score = 0
            for c in reversed([open_close[c] for c in open_chunks]):
                score = score*5 + score_chart[c]
            scores.append(score)

print(sorted(scores)[len(scores)//2])
