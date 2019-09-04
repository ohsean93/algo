import sys

sys.stdin = open("input.txt", "r")


def combi(num_list, size):
    global combi_list
    now_size = len(num_list)
    if size == now_size:
        combi_list.append(num_list)
    else:
        start_num = num_list[-1] + 1
        if start_num >= n:
            return
        elif start_num > size + now_size:
            return
        elif start_num == size + now_size:
            combi_list.append(num_list + list(range(start_num, n)))
        else:
            for next_num in range(start_num, n):
                next_list = num_list + [next_num]
                combi(next_list, size)


n = int(input())
d = n//2
combi_list = []
all_num = list(range(n))
combi([0], d)
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] += matrix[j][i]

min_num = 4500
for case_list in combi_list:
    sum_num = 0
    other_list = []
    for num in all_num:
        if num in case_list:
            continue
        else:
            other_list.append(num)

    for i in range(d):
        for j in range(i+1, d):
            sum_num += (matrix[case_list[i]][case_list[j]] - matrix[other_list[i]][other_list[j]])

    sum_num = abs(sum_num)
    if min_num > sum_num:
        min_num = sum_num

print(min_num)