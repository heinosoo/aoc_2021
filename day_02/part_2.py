with open("input.txt") as f:
    X = 0
    Z = 0
    A = 0
    for line in f.readlines():
        com, h = line.strip().split()
        if com == 'forward':
            X += int(h)
            Z += int(h)*A
        elif com == 'down':
            A += int(h)
        elif com == 'up':
            A -= int(h)
print(X*Z)
