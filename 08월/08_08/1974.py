import sys

sys.stdin = open("input.txt", "r")

T = int(input())
test_num = list('123456789')
small_sqaure_point = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
small_sqaure = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

for test_case in range(T):
    ans = 1
    matrix = [[],[],[],[],[],[],[],[],[]]
    for line_num in range(9):
        line = input().split()
        matrix[line_num] = line
        for num in test_num:
            for num2 in line:
                if num == num2:
                    break
            else:
                ans = 0
                break

    for i in range(9):
        col = [x[i] for x in matrix]

        for num in test_num:
            for num2 in col:
                if num == num2:
                    break
            else:
                ans = 0
                break

    for x,y in small_sqaure_point:
        sqaure = list('123456789')
        index = 0
        for x_dal,y_dal in small_sqaure:
            sqaure[index] = matrix[x+x_dal][y+y_dal]
            index += 1
        
        for num in test_num:
            for num2 in sqaure:
                if num == num2:
                    break
            else:
                ans = 0
                break

    print(test_case+1,ans)