import sys

sys.stdin = open("input.txt", "r")


def combi(use_list, size):
    if use_list:
        now_node = use_list[-1]
    else:
        now_node = -1
    if size - len(use_list) > chicken - now_node:
        return
    elif size - len(use_list) - 1 == (chicken - now_node):
        next_list = use_list + list(range(now_node+1, chicken))
        can_live_list.append(next_list)
    else:
        for next_node in range(now_node+1, chicken):
            next_list = use_list + [next_node]
            if len(next_list) == size:
                can_live_list.append(next_list)
            else:
                combi(next_list, size)


def sum_d_chicken(live_list):
    sum_d = 0
    for p_x, p_y in house:
        min_d = 100
        for index in live_list:
            c_x, c_y = chicken_list[index]
            d = abs(c_x - p_x) + abs(c_y - p_y)
            if d < min_d:
                min_d = d
        sum_d += min_d
    return sum_d


n, m = map(int, input().split())
can_live_list = []
matrix = [0] * n
house = []
chicken_list = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2:
            chicken_list.append((i, j))
        elif line[j] == 1:
            house.append((i, j))

chicken = len(chicken_list)

min_num = 65000
combi([], m)

for case_list in can_live_list:
    temp = sum_d_chicken(case_list)  # type: int
    if temp < min_num:
        min_num = temp
print(min_num)