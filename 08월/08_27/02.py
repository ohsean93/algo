import sys

sys.stdin = open('input.txt', 'r')

vector = [(0, 1), (0, -1), (-1, 0), (1, 0)]

T = int(input())
for test_case in range(1, T+1):
    sum_e = 0
    n = int(input())
    atom_list = dict()
    for i in range(n):
        p_x, p_y, d, e = map(int, input().split())
        atom_list[(2*p_x, 2*p_y)] = [d, e]

    while n > 0:
        new_atom_list = dict()
        for key, value in atom_list.items():
            p_x, p_y = key
            d, e = value[0], value[1]
            x, y = p_x + vector[d][0], p_y + vector[d][1]
            if 2000 > x > -2000 and 2000 > y > -2000:
                if new_atom_list.get((x, y)):
                    new_atom_list[(x, y)][0] = 4
                    new_atom_list[(x, y)][1] = new_atom_list[(x, y)][1] + e
                else:
                    new_atom_list[(x, y)] = value

        atom_list = dict()
        for key, value in new_atom_list.items():
            d, e = value[0], value[1]
            if d == 4:
                sum_e += e
            else:
                atom_list[key] = value

        n = len(atom_list)

    print(sum_e)



