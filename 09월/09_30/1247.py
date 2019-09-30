import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    point_list = []
    for i, num in enumerate(map(int, input().split())):
        if i % 2:
            point_list.append((temp, num))
        else:
            temp = num
    print(point_list)