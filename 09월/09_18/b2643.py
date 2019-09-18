import sys

sys.stdin = open('input.txt', 'r')
n = int(input())
for _ in range(n):
    list(map(int, input().split())).sort()