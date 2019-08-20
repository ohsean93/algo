import sys

sys.stdin = open("input.txt", "r")

vactor = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def turn(dot_list):
    add_dot_list = []
    center_x, center_y = dot_list[-1]
    for a, b in dot_list[:-1]:
        add_dot_list.append((- b + center_y + center_x, a - center_x + center_y))
    return reversed(add_dot_list)


n = int(input())

all_dot = dict()
for case in range(n):
    x, y, d, g = map(int, input().split())
    dot_1 = (x + vactor[d][0], y + vactor[d][1])
    dots = [(x, y), dot_1]
    for _ in range(g):
        dots += turn(dots)

    for x, y in dots:
        if all_dot.get(x):
            if y not in all_dot[x]:
                all_dot[x].add(y)
        else:
            all_dot[x] = {y}

cnt = 0
for x in all_dot.keys():
    if all_dot.get(x + 1):
        edge = all_dot[x] & all_dot[x+1]
        for y in edge:
            if y+1 in edge:
                cnt += 1

print(cnt)