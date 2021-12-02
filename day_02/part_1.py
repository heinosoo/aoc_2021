with open("input.txt") as f:
    X = 0
    Z = 0
    for line in f.readlines():
        com, h = line.strip().split()
        if com == 'forward':
            X += int(h)
        elif com == 'down':
            Z += int(h)
        elif com == 'up':
            Z -= int(h)
print(X*Z)
