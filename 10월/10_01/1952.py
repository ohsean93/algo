import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    d, m, s, y = map(int, input().split())
    swimming = list(map(int, input().split()))
    swimming = list(map(lambda x: x*d, swimming)) + [0, 0]
    # print(swimming)
    for i in range(14):
        if swimming[i] > m:
            swimming[i] = m

    stack = [(0, 0)]
    max_num = 0
    while stack:
        sum_num, sp = stack.pop()
        for i in range(sp, 14):
            if sum(swimming[i:min(i+3, 14)]) > s:
                next_sum_num = sum_num + (sum(swimming[i:i+3]) - s)
                next_sp = i + 3
                stack.append((next_sum_num, next_sp))
                if next_sum_num > max_num:
                    max_num = next_sum_num

    all_price = min(sum(swimming) - max_num, y)
    print('#{} {}'.format(test_case, all_price))
