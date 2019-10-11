import sys

sys.stdin = open('input.txt', 'r')


def in_order(now_node):
    global cnt, num_list
    if 2 * now_node < n:
        in_order(2 * now_node)
        cnt += 1
        num_list[now_node] = cnt
        in_order(2 * now_node + 1)
    elif 2 * now_node == n:
        in_order(2 * now_node)
        cnt += 1
        num_list[now_node] = cnt
    else:
        cnt += 1
        num_list[now_node] = cnt


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_list = [0] * (n + 1)
    cnt = 0
    in_order(1)
    print('#{} {}'.format(num_list[1], num_list[n//2]))