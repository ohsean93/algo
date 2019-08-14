import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(T):
    k, count = int(input()), 0
    matrix = [0] * 8

    for i in range(8):
        line = input()
        matrix[i] = line
        for j in range(8-k+1):
            check_str = line[j:j+k]
            for index in range((k+1)//2):
                if check_str[index] != check_str[-index-1]:
                    break
            else:
                count += 1

    for j in range(8):
        col = [line[j] for line in matrix]
        for j in range(8 - k + 1):
            check_str = col[j:j + k]
            for index in range((k + 1) // 2):
                if check_str[index] != check_str[-index - 1]:
                    break
            else:
                count += 1

    print('#{} {}'.format(test_case+1, count))