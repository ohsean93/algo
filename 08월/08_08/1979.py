import sys

sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(T):

    n, k = map(int,input().split())
    count = 0

    zore_line = ''
    for i in range(n+2):
        zore_line += '0'

    check_str = '0'
    for i in range(k):
        check_str += '1'
    check_str += '0'

    matrix = list(zore_line)
    matrix[0] = zore_line
    matrix[n+1] = zore_line

    for line_num in range(n):
        line = '0' + input().replace(' ','') + '0'
        matrix[line_num + 1] = line
        for i in range(n-k+1):
            if line[i:i+k+2] == check_str:
                count += 1
        

    for i in range(n+2):
        col = ''
        for x in matrix:
            col += x[i]
        for i in range(n-k+1):
            if col[i:i+k+2] == check_str:
                count += 1

    print('#{} {}'.format(test_case+1, count))