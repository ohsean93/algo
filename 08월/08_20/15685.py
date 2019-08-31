import sys

sys.stdin = open("input.txt", "r")

vactor = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 최초 방향 설정


# 점들을 불러와 종점을 기준으로 회전
def turn(dot_list):
    add_dot_list = []
    center_x, center_y = dot_list[-1]
    for a, b in dot_list[:-1]:
        add_dot_list.append((- b + center_y + center_x, a - center_x + center_y))
    # 가장 먼 점(원점)은 가장 먼저 뽑히므로 반대로 넣는다.
    return reversed(add_dot_list)


n = int(input())

all_dot = dict()
for case in range(n):
    x, y, d, g = map(int, input().split())
    dot_1 = (x + vactor[d][0], y + vactor[d][1])
    dots = [(x, y), dot_1]
    # 세대만큼 turn 호출해 이를 점 리스트에 넣는다.
    for _ in range(g):
        dots += turn(dots)

    # 딕션어리로 x:key y:value y는 셋으로 관리(중복 관리)
    for x, y in dots:
        if all_dot.get(x):
            if y not in all_dot[x]:
                all_dot[x].add(y)
        else:
            all_dot[x] = {y}

cnt = 0
# x번째 x+1번째 열에서 중복으로 있는 y값 중 연속적인 것을 찾는 부분
for x in all_dot.keys():
    if all_dot.get(x + 1):
        edge = all_dot[x] & all_dot[x+1]
        for y in edge:
            if y+1 in edge:
                cnt += 1

print(cnt)