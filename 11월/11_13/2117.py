import sys

sys.stdin = open('input.txt', 'r')


def distance(p_x, p_y, h_x, h_y):
    return abs(p_x - h_x) + abs(p_y - h_y)


cost_per_d = [0]
base_count_list = [0 for __ in range(42)]
for d in range(1, 42):
    cost_per_d.append(-(d**2 + (d-1)**2))

T = int(input())
for test_case in range(1, T+1):
    ans = 0
    n, m = map(int, input().split())
    house = []
    for i in range(n):
        line = input().split()
        for j, num in enumerate(line):
            if num == '1':
                house.append((i, j))

    for i in range(n):
        for j in range(n):
            d_list = [distance(i, j, *k) + 1 for k in house]
            benefit = cost_per_d.copy()[:2*n+2]
            count_list = base_count_list.copy()[:2*n+2]
            for d in d_list:
                for idx in range(d, 2 * n + 1):
                    benefit[idx] += m
                    count_list[idx] += 1
            for d in range(2*n+1, 0, -1):
                if benefit[d] >= 0:
                    ans = max(ans, count_list[d])
    print('#{} {}'.format(test_case, ans))