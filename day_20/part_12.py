def enhance(image, x, y):
    return iea[int(image[y-1][x-1:x+2]+image[y][x-1:x+2]+image[y+1][x-1:x+2], 2)]


with open('input.txt') as f:
    iea = f.readline().strip().replace('.', '0').replace('#', '1')
    image = f.read().strip().replace('.', '0').replace('#', '1').split('\n')

for i in range(50):
    p = str(i % 2 * int(iea[0]))  # Damn you, simple example..
    new = [p*(len(image[0])+4), ]*(len(image)+4)
    padded = [2*p+line+2*p for line in image]
    padded = [p*(len(image[0])+4), ]*2+padded+[p*(len(image[0])+4), ]*2
    image = [''.join([enhance(padded, j, i) for j in range(1, len(padded[0])-1)])
             for i in range(1, len(padded)-1)]

print(sum([sum([1 for c in line if c == '1']) for line in image]))
