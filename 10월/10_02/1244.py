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
    goal = int(''.join(goal_list))

    can_change_case = list(itertools.combinations(range(n), 2))
    stack = [origin]
    i = 0
    ans = int(origin_str)
    for i in range(can_change):
        p = 0
        new_stack = []
        for now_prise in stack:
            prise = int(''.join(now_prise))
            for x, y in can_change_case:
                next_prise = now_prise.copy()
                next_prise[x], next_prise[y] = next_prise[y], next_prise[x]
                p = int(''.join(next_prise))
                if p < ans:
                    continue
                if next_prise in new_stack:
                    continue
                else:
                    new_stack.append(next_prise)
                if ans < p:
                    ans = p
                if p == goal:
                    break
            if p == goal:
                break
        if p == goal:
            break
        stack = new_stack

    if (can_change-i) % 2:
        print('#{} {}'.format(test_case, ans))
    else:
        goal_list[-1], goal_list[-2] = goal_list[-2], goal_list[-1]
        print('#{} {}'.format(test_case, ''.join(goal_list)))
