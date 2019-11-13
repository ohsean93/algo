import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
# for test_case in range(1):
    n = int(input())
    people_list = []
    stair_list = []

    for i in range(n):
        line = input().split()
        for j, num in enumerate(line):
            if num == '1':
                people_list.append((i, j))
            elif num != '0':
                stair_list.append((i, j, int(num)))

    p = len(people_list)
    m_t = []
    answer = 999999
    for p_x, p_y in people_list:
        temp = []
        for s_x, s_y, use_time in stair_list:
            temp.append(abs(p_x - s_x) + abs(p_y - s_y))
        m_t.append(temp)
    for k in range(p + 1):
        for case in combinations(range(p), k):
            arrive_move_stair = [[stair_list[0][2]], [stair_list[1][2]]]
            for p_num in range(p):
                if p_num in case:
                    arrive_move_stair[0].append(m_t[p_num][0])
                else:
                    arrive_move_stair[1].append(m_t[p_num][1])
            temp_num = 0
            for stair_queue in arrive_move_stair:
                cost = stair_queue[0]
                stair_queue = stair_queue[1:]
                stair_queue.sort()
                m = len(stair_queue)
                if m == 0:
                    continue
                elif m > 3:
                    hidden_num = m % 3

                    for index in range(hidden_num, m, 3):
                        next_can_start = stair_queue[index - 3] + cost
                        if next_can_start > stair_queue[index]:
                            stair_queue[index] = next_can_start

                local_max = stair_queue[-1] + cost
                if temp_num < local_max:
                    temp_num = local_max
            if temp_num < answer:
                answer = temp_num

    print('#{} {}'.format(test_case, answer+1))

