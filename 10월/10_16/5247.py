import sys

sys.stdin = open('input.txt', 'r')
maximal_num = 10 ** 6 + 1


def cal(origin_num):
    a = [origin_num + 1, origin_num - 1, origin_num * 2, origin_num - 10]
    return_list = []
    for next_num in a:
        if 0 < next_num < maximal_num:
            return_list.append(next_num)
    return return_list


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    check_num = [0] * maximal_num

    stack = [n]
    cnt = 0
    ans = -1

    while stack:
        new_stack = []
        if check_num[m] != 0:
            ans = cnt
            break
        cnt += 1
        for num in stack:
            temp = cal(num)
            for new_num in temp:
                if check_num[new_num] == 0:
                    check_num[new_num] = cnt
                    new_stack.append(new_num)
        stack = new_stack

    print('#{} {}'.format(test_case, ans))