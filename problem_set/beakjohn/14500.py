def check_num(size_x, size_y, n, m, shape, matrix):
    max_num = 0
    for x in range(n - size_x + 1):
        for y in range(m - size_y + 1):
            num = sum([matrix[x+i][y+j] for i, j in shape])
            if max_num < num:
                max_num = num

    return max_num


def shape_checker(n, m, matrix, **kwarg):
    max_num = 0
    for type_num in range(len(kwarg['type'])):
        num = check_num(kwarg['size'][type_num][0], kwarg['size'][type_num][1], n, m, kwarg['type'][type_num], matrix)
        if max_num < num:
            max_num = num

    return max_num


line = {
    'type': [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],
    'size': [(1, 4), (4, 1)]
}

L = {
    'type': [[(0, 0), (0, 1), (0, 2), (1, 2)], [(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (0, 2), (1, 0)],
             [(1, 0), (1, 1), (1, 2), (0, 0)],
             [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 1), (1, 1), (2, 1), (2, 0)],
             [(0, 0), (1, 0), (2, 0), (0, 1)], [(0, 1), (1, 1), (2, 1), (0, 0)]],
    'size': [(2, 3), (2, 3), (2, 3), (2, 3), (3, 2), (3, 2), (3, 2), (3, 2)]
}

square = {
    'type': [[(0, 0), (0, 1), (1, 1), (1, 0)]],
    'size': [(2, 2)]
}

z = {
    'type': [[(0, 0), (0, 1), (1, 1), (1, 2)], [(1, 0), (0, 1), (1, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (2, 1)],
             [(0, 1), (1, 0), (1, 1), (2, 0)]],
    'size': [(2, 3), (2, 3), (3, 2), (3, 2)]
}

t = {
    'type': [[(0, 0), (0, 1), (0, 2), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)],
             [(0, 1), (1, 1), (2, 1), (1, 0)]],
    'size': [(2, 3), (2, 3), (3, 2), (3, 2)]
}

n1, m1 = map(int, input().split())
matrix1 = []
for row in range(n1):
    matrix1.append(list(map(int, input().split())))

ans = max(shape_checker(n1, m1, matrix1, **line), shape_checker(n1, m1, matrix1, **L),
          shape_checker(n1, m1, matrix1, **square), shape_checker(n1, m1, matrix1, **z),
          shape_checker(n1, m1, matrix1, **t))

print(ans)
