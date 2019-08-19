import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())
    ans = ''
    matrix = [0] * n

    for i in range(n):
        line = input()
        matrix[i] = line
        for j in range(n-k+1):
            check_str = line[j:j+k]
            for index in range((k+1)//2):
                if check_str[index] != check_str[-index-1]:
                    break
            else:
                ans = check_str

    if ans == '':
        for i in range(n):
            col = [line[i] for line in matrix]
            for j in range(n - k + 1):
                check_str = col[j:j + k]
                for index in range((k + 1) // 2):
                    if check_str[index] != check_str[-index - 1]:
                        break
                else:
                    ans = ''.join(check_str)

    print('#{} {}'.format(test_case+1, ans))