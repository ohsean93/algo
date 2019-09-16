import sys

sys.stdin = open('input.txt', 'r')

ans = []
T = int(input())
for test_case in range(1, T + 1):
    str_origin = input()
    while len(str_origin) != 1:
        str_origin = str(sum(map(int, str_origin)))
    ans.append('#{} {}'.format(test_case, str_origin))

print('\n'.join(ans))