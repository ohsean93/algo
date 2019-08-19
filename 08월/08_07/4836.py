import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    zero_line = [0]*10
    matrix = [[]]*10
    for line_num in range(10):
        matrix[line_num] = zero_line.copy()
    count = 0

    for case in range(int(input())):
        x_min, y_min, x_max, y_max, color = map(int, input().split())
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                matrix[x][y] += color
        
    for x in range(10):
        for y in range(10):
            if matrix[x][y] == 3:
                count += 1
            
    print('#{} {}'.format(test_case+1,count))