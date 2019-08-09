import sys

sys.stdin = open("input.txt", "r")
# T = int(input())
# for test_case in range(T):
#
#     n, m = map(int, input().split())
#     list_line = [0]*(m+1)
#     for i in range(m):
#         a, b = map(int, input().split())
#         if a > b:
#             list_line[b] += 1 << a
#         else:
#             list_line[a] += 1 << b
#
#     count_num = 0
#
#     for i in range(1, m+1):
#         for j in range(i+1, m+1):
#             if list_line[i] & 1 << j:
#                 for k in range(j+1, m+1):
#                     if list_line[i] & 1 << k:
#                         if list_line[j] & 1 << k:
#                             count_num += 1
#
#     print('#{} {}'.format(test_case+1, count_num))

T = int(input())
for test_case in range(T):

    n, m = map(int, input().split())
    list_line = []
    for i in range(n+1):
        list_line += [[]].copy()
    for i in range(m):
        a, b = map(int, input().split())
        if a > b:
            list_line[b].append(a)
        else:
            list_line[a].append(b)

    count_num = 0

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in list_line[i]:
                for k in range(j+1, n+1):
                    if k in list_line[i]:
                        if k in list_line[j]:
                            count_num += 1

    print('#{} {}'.format(test_case+1, count_num))