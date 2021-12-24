execute = {'add': lambda x, y: x + y,
           'mul': lambda x, y: x * y,
           'div': lambda x, y: x // y,
           'mod': lambda x, y: x % y,
           'eql': lambda x, y: int(x == y)}

def serial(i=0, mem={'w': 0, 'x': 0, 'y': 0, 'z': 0}):
    if tuple(mem.values())+(i,) in cache:
        return 0
    if i >= len(cmd_blocks):
        return int(not mem['z'])
    for n in range(9, 0, -1):
        new_mem = mem.copy()
        new_mem[cmd_blocks[i][0]] = n
        for cmd, a, b in cmd_blocks[i][1]:
            if type(b) == int:
                new_mem[a] = execute[cmd](new_mem[a], b)
            else:
                new_mem[a] = execute[cmd](new_mem[a], new_mem[b])
        m = serial(i+1, new_mem)
        if m:
            return str(n)+str(m)
    cache[tuple(mem.values())+(i,)] = 0
    return 0

with open('input.txt') as f:
    cmds = [line.strip().split(' ') for line in f.readlines()]
    cmds = [c[:2]+[int(c[2])] if len(c) == 3 and c[2] not in 'wxyz' else c for c in cmds]
    index = [i for i, (cmd, *_) in enumerate(cmds) if cmd == 'inp'] + [len(cmds)]
    cmd_blocks = [(cmds[index[i]][1], cmds[index[i]+1:index[i+1]])
                  for i in range(len(index)-1)]

cache = {}
print(serial()[:-1])
