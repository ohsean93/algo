nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
matrix = dict()
height_set = set()
x_set = set()
for node in nodeinfo:
    x, y = node[0], node[1]
    height_set.add(y)
    x_set.add(x)
    if matrix.get(y):
        matrix[y] = matrix[y] + [x]
    else:
        matrix[y] = [x]

print(matrix)
height_set = sorted(list(height_set))[::-1]
x_set = sorted(list(x_set))
print(height_set)


def make_tree(L, R, b, h_index):
    d = 0
    if h_index >= len(height_set):
        return []
    h = height_set[h_index]
    print(L, R, h)
    if L == R:
        if L in matrix[h]:
            return []
    else:
        for num in matrix[h]:
            if L < num < R:
                d = num
                print(d)
                break
        else:
            return []
    print((b, d))
    return [(b, d)] + make_tree(L, d, d, h_index + 1) + make_tree(d, R, d, h_index + 1)


print(make_tree(0, 14, 0, 0))

array = make_tree(0, 14, 0, 0)



edges = {}
