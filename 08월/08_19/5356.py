import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    str_lines = [0] * 5
    cnt_lines = [0] * 5
    max_num = 0

    for i in range(5):
        str_lines[i] = input()
        cnt_lines[i] = len(str_lines[i])
        if max_num < cnt_lines[i]:
            max_num = cnt_lines[i]

    ans = ''

    for i in range(max_num):
        for j, line in enumerate(str_lines):
            if i < cnt_lines[j]:
                ans += line[i]

    print('#{} {}'.format(test_case+1, ans))
