import sys

sys.stdin = open("input.txt", "r")

vector = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

point = [0, 0]
point_list = [[0, 0]]
num = int(input())
set_x = set()
set_y = set()

for _ in range(6):
    d, n = map(int, input().split())
    dal_x, dal_y = n*vector[d][0], n * vector[d][1]
    point[0] += dal_x
    point[1] += dal_y
    set_x.add(point[0])
    set_y.add(point[1])
    point_list.append(point.copy())

list_x = sorted(list(set_x))
mid_x = list_x.pop(1)
list_y = sorted(list(set_y))
mid_y = list_y.pop(1)

sum_num = 0
for i in list_x:
    for j in list_y:
        if [i, j] in point_list:
            sum_num += (abs(mid_x-i)*abs(mid_y-j))

ans = sum_num*num
print(ans)

