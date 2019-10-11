import sys

sys.stdin = open('input.txt', 'r')


def find_num(now_node):
    global n, num_list
    if 2 * now_node < n:
        return find_num(2 * now_node) + find_num(2 * now_node + 1)
    elif 2 * now_node == n:
        return num_list[n]
    else:
        return num_list[now_node]


T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    num_list = [0] * (n+1)
    for _ in range(m):
        ind, num = map(int, input().split())
        num_list[ind] = num
    print('#{} {}'.format(test_case, find_num(l)))