import sys

sys.stdin = open('input.txt', 'r')

T = 10


def in_order_out(now_idx):
    global str_list, n, answer
    if 2 * now_idx < n:
        in_order_out(2 * now_idx)
        answer += str_list[now_idx]
        in_order_out(2 * now_idx + 1)
    elif 2 * now_idx == n:
        in_order_out(2 * now_idx)
        answer += str_list[now_idx]
    else:
        answer += str_list[now_idx]


for test_case in range(1, T + 1):
    answer = ''
    n = int(input())
    str_list = [0] * (n + 1)
    for i in range(n):
        input_list = list(input().split())
        str_list[i+1] = input_list[1]
    in_order_out(1)
    print('#{} {}'.format(test_case, answer))

