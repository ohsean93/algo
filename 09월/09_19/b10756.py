import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
dot_list = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    dot_list[i] = (x, y)

m = int(input())
olive_list = [0] * m
for j in range(m):
    x, y = map(int, input().split())
    olive_list[j] = (x, y)

print(dot_list)
print(olive_list)