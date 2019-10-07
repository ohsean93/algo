import sys

sys.stdin = open('input.txt', 'r')

memo = [0] * 101
memo[0] = memo[1] = memo[2] = memo[3] = 1
memo[4] = memo[5] = 2
for i in range(6, 101):
    memo[i] = memo[i-1] + memo[i-5]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(memo[n])
