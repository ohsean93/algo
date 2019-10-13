import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    max_c = 0
    N, K = map(int, input().split())
    temp = [(0, 0)]
    for _ in range(N):
        v, c = map(int, input().split())
        new_temp = []
        for sum_v, sum_c in temp:
            next_v = sum_v + v
            next_c = sum_c + c
            if next_v <= K:
                new_temp.append((next_v, next_c))
                if max_c < next_c:
                    max_c = next_c
        temp += new_temp
    print('#{} {}'.format(test_case, max_c))