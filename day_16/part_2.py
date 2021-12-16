from numpy import prod


def parse(P=0):
    # version = int(packet[P:P+3], 2)
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
        return P, int(L, 2)
    else:
        if packet[P] == '0':
            len_b = int(packet[P+1:P+16], 2)
            new_P = P + 16
            values = []
            while new_P < P + 16 + len_b:
                new_P, new_value = parse(new_P)
                values.append(new_value)
            return new_P, calculate(typeID, values)
        else:
            len_p = int(packet[P+1:P+12], 2)
            new_P = P + 12
            values = []
            for i in range(len_p):
                new_P, new_value = parse(new_P)
                values.append(new_value)
            return new_P, calculate(typeID, values)


def calculate(typeID, values):
    if typeID == 0:
        return sum(values)
    elif typeID == 1:
        return prod(values)
    elif typeID == 2:
        return min(values)
    elif typeID == 3:
        return max(values)
    elif typeID == 5:
        return int(values[0] > values[1])
    elif typeID == 6:
        return int(values[0] < values[1])
    elif typeID == 7:
        return int(values[0] == values[1])


with open('input.txt') as f:
    # This removes zeroes from the beginning of the input, so some examples fail.
    packet = "{0:b}".format(int(f.readline().strip(), 16))
    packet = ((4 - len(packet) % 4) % 4)*'0' + packet  # Beginning zeroes..

print(parse()[1])
