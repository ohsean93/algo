n = 5
matrix = [...]
list_matrix = []

for i in range(n):
    list_matrix += matrix[i]
sort_list = sorted(list_matrix)

add_vactor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
vactor_check = 0
len_vactor = n
real_len = 0
len_vactor_check = 1
line, row = 0, 0
for i in range(0, n**2):
    matrix[line][row] = sort_list[i]
    real_len +=1
    if len_vactor == real_len:
        vactor_check +=1
        vactor_check %=4
        len_vactor_check += 1
        if len_vactor_check == 2:
            len_vactor -=1
            len_vactor_check = 0
        real_len = 0

    line += add_vactor[vactor_check][1]
    row += add_vactor[vactor_check][0]

for line in range(n):
    print(' '.join(matrix[line]))