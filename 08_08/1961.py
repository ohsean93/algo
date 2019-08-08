import sys

def turn_mat(size,mat):
    out_matrix = [[]] * size
    
    for i in range(size-1,-1,-1):
        new_line = ''
        for line in mat[::-1]:
            line_list = list(line)
            new_line += line_list[i]
        out_matrix[i] = new_line
    return out_matrix
        

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    n = int(input())
    matrix = [[]] * n
    for line_num in range(n):
        line = input().replace(' ','')
        matrix[line_num] = line

    matrix_turn1 = turn_mat(n, matrix)
    matrix_turn2 = turn_mat(n, matrix_turn1)
    matrix_turn3 = turn_mat(n, matrix_turn2)

    print('#{}'.format(test_case+1))

    for i in range(n):
        print(matrix_turn1[i], matrix_turn2[i], matrix_turn3[i])




    