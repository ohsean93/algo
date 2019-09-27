import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):

    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    sorted(height, reverse=True)
    memo = [0] * (2**n)
    checker = 0
    min_num = 20000000

    while checker < 2**n:
        check_list = bin(checker)[3:]
        l = len(check_list)
        k = checker - 2**l
        if memo[k] or k == 0:
            sub_sum = memo[k] + height[l]
            if sub_sum < b:
                memo[checker] = sub_sum
            else:
                if min_num > sub_sum:
                    min_num = sub_sum

        checker += 1

    print('#{} {}'.format(test_case, min_num - b))