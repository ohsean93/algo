# a = list(map(int, '123456789'))+[10]
# cnt = 0
#
#
# def dfs(visit_list, p):
#     global cnt
#     cnt += 1
#     for num in range(p+1, 10):
#         if sum(visit_list) + num == 10:
#             print(visit_list + [num])
#         elif sum(visit_list) + num > 10:
#             return
#         else:
#             dfs(visit_list + [num], num)
#
#
# dfs([], 0)
# print(cnt)
matrix = ['123', '456', '789']



def right_turn():
    map_list = matrix.copy()
    for col in range(3):
        matrix[2 - col] = [line[col] for line in map_list]


def left_turn():
    map_list = matrix.copy()
    for col in range(3):
        matrix[col] = [line[col] for line in map_list[::-1]]


right_turn()
for i in range(3):
    print(matrix[i])

print()

left_turn()
for i in range(3):
    print(matrix[i])