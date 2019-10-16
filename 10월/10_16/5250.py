import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    max_num = 10 ** 7
    matrix = [list(map(int, input().split())) for _ in range(n)]