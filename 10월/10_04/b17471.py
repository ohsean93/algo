import sys

sys.stdin = open('input.txt', 'r')

import itertools


def dfs(my_list):
    global linked_list
    visit = [0] * (n+1)
    for num in my_list:
        visit[num] = 1
    visit[my_list[0]] = 0
    stack = [my_list[0]]
    while stack:
        num = stack.pop()
        for j in linked_list[num]:
            if visit[j] and j in my_list:
                visit[j] = 0
                stack.append(j)
    if sum(visit):
        return False
    return True


n = int(input())
people = [0] + list(map(int, input().split()))
linked_list = [[] for _ in range(n+1)]
min_num = 1000

for i in range(1, n+1):
    linked_list[i] = list(map(int, input().split()))[1:]

for k in range(1, (n+1)//2 + 1):
    all_case = list(itertools.combinations(list(range(1, n+1)), k))
    for case in all_case:
        sub_case = []
        sum_num = 0
        for v in list(range(1, n+1)):
            if v in case:
                sum_num += people[v]
            else:
                sum_num -= people[v]
                sub_case.append(v)
        if dfs(case) and dfs(sub_case):
            if min_num > abs(sum_num):
                min_num = abs(sum_num)

if min_num == 1000:
    min_num = -1
print(min_num)