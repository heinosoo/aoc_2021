open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_chart = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('input.txt') as f:
    score = 0
    for line in f.readlines():
        open_chunks = []
        for c in line.strip():
            if c in open_close:
                open_chunks.append(c)
            else:
                if open_close[open_chunks.pop()] != c:
                    score += score_chart[c]
                    break
print(score)
