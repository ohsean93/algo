import sys

sys.stdin = open('input.txt', 'r')

T = 10


def cal(a, b, char):
    if char == '+':
        return a + b
    elif char == '-':
        return a - b
    elif char == '/':
        return a / b
    elif char == '*':
        return a * b


def post_order(now_node):
    now_node = int(now_node)
    if tree.get(now_node):
        l_num = post_order(tree[now_node][0])
        r_num = post_order(tree[now_node][1])
        return cal(l_num, r_num, data_list[now_node])
    else:
        return int(data_list[now_node])


for test_case in range(1, T + 1):
    n = int(input())
    tree = dict()
    data_list = [0] * (n+1)
    for i in range(n):
        input_list = list(input().split())
        if len(input_list) == 2:
            p_node, data = input_list
            tree[int(p_node)] = []
        elif len(input_list) == 3:
            p_node, data, l_node = input_list
            tree[int(p_node)] = [l_node]
        else:
            p_node, data, l_node, r_node = input_list
            tree[int(p_node)] = [l_node, r_node]
        data_list[int(p_node)] = data
    print('#{} {:0.0f}'.format(test_case, post_order(1)))
