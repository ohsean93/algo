import sys

sys.stdin = open('input.txt', 'r')

import itertools

T = int(input())
for test_case in range(1, T + 1):
    origin_str, can_change = input().split()
    can_change = int(can_change)
    n = len(origin_str)
    if n == 1:
        print('#{} {}'.format(test_case, origin_str))
        continue
    origin = list(origin_str)
    goal_list = sorted(origin, reverse=True)

    cnt = 0
    for i in range(n):
        if origin[i] == goal_list[i]:
            continue
        else:
            cnt += 1
            j = origin.index(goal_list[i], i)
            origin[i], origin[j] = origin[j], origin[i]

    if cnt == 0:
        print('#{} {}'.format(test_case, origin_str))
        continue
    if cnt < can_change:
        if (can_change-cnt) % 2:
            goal_list[-1], goal_list[-2] = goal_list[-2], goal_list[-1]
            print('#{} {}'.format(test_case, ''.join(goal_list)))
            continue
        else:
            print('#{} {}'.format(test_case, ''.join(goal_list)))
            continue

    max_num = 0
    origin = list(origin_str)
    num_list = list(range(n))
    all_can_change = list(itertools.combinations(num_list, 2))
    all_case = list(itertools.permutations(all_can_change, can_change))
    for case in all_case:
        copy_origin = origin.copy()
        for n_1, n_2 in case:
            copy_origin[n_1], copy_origin[n_2] = copy_origin[n_2], copy_origin[n_1]
        case_num = int(''.join(copy_origin))
        if max_num < case_num:
            max_num = case_num
    print('#{} {}'.format(test_case, max_num))
