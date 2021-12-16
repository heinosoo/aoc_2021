def parse(P=0):
    version = int(packet[P:P+3], 2)
    typeID = int(packet[P+3:P+6], 2)
    P += 6
    if typeID == 4:
        L = ''
        while True:
            a, b = packet[P], packet[P+1:P+5]
            L += b
            P += 5
            if a == '0':
                break
        return P, version
    else:
        if packet[P] == '0':
            len_b = int(packet[P+1:P+16], 2)
            new_P = P + 16
            while new_P < P + 16 + len_b:
                new_P, new_version = parse(new_P)
                version += new_version
            return new_P, version
        else:
            len_p = int(packet[P+1:P+12], 2)
            new_P = P + 12
            for i in range(len_p):
                new_P, new_version = parse(new_P)
                version += new_version
            return new_P, version


with open('input.txt') as f:
    packet = "{0:b}".format(int(f.readline().strip(), 16))
    packet = ((4 - len(packet) % 4) % 4)*'0' + packet  # Beginning zeroes..

print(parse()[1])
