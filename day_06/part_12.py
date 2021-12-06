import numpy as np

fish = np.loadtxt('input.txt', int, delimiter=',')
histogram = [np.count_nonzero(fish == 8-i) for i in range(9)]
for day in range(256):
    new = histogram.pop()
    histogram.insert(0, new)
    histogram[2] += new
sum(histogram)
