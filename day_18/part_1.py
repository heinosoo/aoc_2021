def add_right(left, n):
    if type(left) == int:
        return left+n
    else:
        return [left[0], add_right(left[1], n)]


def add_left(right, n):
    if type(right) == int:
        return right+n
    else:
        return [add_left(right[0], n), right[1]]


def split(n, reduced=False):
    if reduced or (type(n) == int and n < 10):
        return n, reduced
    elif type(n) == int:
        return [n//2, (n+1)//2], True
    else:
        left, reduced = split(n[0], reduced)
        right, reduced = split(n[1], reduced)
        return [left, right], reduced


def explode(n, L=0, reduced=False):
    if reduced or type(n) == int:
        return n, 0, 0, reduced
    if L == 4:
        return 0, *n, True
    else:
        left, a, b, reduced = explode(n[0], L+1, reduced)
        right, c, d, reduced = explode(n[1], L+1, reduced)
        left = add_right(left, c)
        right = add_left(right, b)
        return [left, right], a, d, reduced


def add(a, b):
    A = [a, b]
    while True:
        A, _, _, reduced = explode(A)
        if not reduced:
            A, reduced = split(A)
        if not reduced:
            break
    return A


def magnitude(n):
    if type(n) == int:
        return n
    else:
        return 3*magnitude(n[0]) + 2*magnitude(n[1])


with open('input.txt') as f:
    numbers = [eval(line) for line in f.readlines()]  # Being lazy here.

S = numbers[0]
for n in numbers[1:]:
    S = add(S, n)

print(magnitude(S))
