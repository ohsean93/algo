import sys

sys.stdin = open("input.txt", "r")
check_list = []
for num in range(142):
    check_list.append(num*(num+1)//2)


def change_xy(num):
    n, d = 0, 0
    for i, checker in enumerate(check_list):
        if num <= checker:
            n = i
            d = checker - num
            break

    p_x, p_y = (n - d), (1 + d)
    return p_x, p_y


def change_num(p_x, p_y):
    n = p_x + p_y - 1
    d = p_y - 1
    num = n*(n+1)//2 - d
    return num

T = int(input())
for test_case in range(1, T + 1):
    num_1, num_2 = map(int, input().split())
    x_1, y_1 = change_xy(num_1)
    x_2, y_2 = change_xy(num_2)

    ans = change_num(x_1 + x_2, y_1 + y_2)
    print('#{} {}'.format(test_case, ans))