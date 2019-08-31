import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    str_origin = input()
    ans = 'Exist'
    if '*' in str_origin:
        str_list = str_origin.split('*')
        a, b = str_list[0], str_list[-1]
        n = min(len(a), len(b))
        if a[:n] != b[::-1][:n]:
            ans = 'Not exist'
    else:
        if str_origin != str_origin[::-1]:
            ans = 'Not exist'
    print('#{} {}'.format(test_case+1, ans))