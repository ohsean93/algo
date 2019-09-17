import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    input_list = list(input().split())
    temp = input_list.pop()
    if temp in input_list:
        input_list.pop(input_list.index(temp))
        ans = input_list[0]
    else:
        ans = temp
    print('#{} {}'.format(test_case, ans))