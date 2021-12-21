with open('input.txt') as f:
    pos = [int(line[-2]) for line in f.readlines()]

score = [0, 0]
die = 1
player = 0
for i in range(1000):
    roll = (die-1) % 100 + 1 + (die) % 100+1 + (die+1) % 100+1
    die = (die+2) % 100+1
    pos[player] = (pos[player]+roll-1) % 10 + 1
    score[player] += pos[player]
    if score[player] >= 1000:
        print((i+1)*3*score[player-1])
        break
    player = (player + 1) % 2
