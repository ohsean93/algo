import sys

sys.stdin = open("input.txt", "r")


def palindrome(check_str, num):
    n = len(check_str)
    for index in range((n+1)//2):
        if check_str[index] != check_str[-index-1]:
            return num
    else:
        return n


T = 10
for test_case in range(T):
    t, max_len = input(), 1
    matrix = [0] * 100

    for i in range(100):
        line = input()
        matrix[i] = line
        for j in range(100):
            for k in range(j+max_len, 100):
                check_str = line[j:k+1]
                n = len(check_str)
                for index in range((n + 1) // 2):
                    if check_str[index] != check_str[-index - 1]:
                        break
                else:
                    max_len =  n





    for i in range(100):
        col = [line[i] for line in matrix]
        for j in range(100):
            for k in range(j + max_len, 100):
                check_str = col[j:k+1]
                n = len(check_str)
                for index in range((n + 1) // 2):
                    if check_str[index] != check_str[-index - 1]:
                        break
                else:
                    max_len =  n

    print('#{} {}'.format(test_case+1, max_len))