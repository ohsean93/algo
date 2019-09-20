import sys
import time
sys.stdin = open("input.txt", "r")

con_matrix = [[0] * 21 for _ in range(21)]


def conbi(n_num, r_num):
    if r_num % n_num:
        pass
    else:
        return 1

    if con_matrix[n_num][r_num]:
        return con_matrix[n_num][r_num]
    else:
        return conbi(n_num - 1, r_num - 1) + conbi(n_num - 1, r_num)


def conbi_2(n_num, r_num):
    return_num = 1
    for num in range(r_num + 1, n_num + 1):
        return_num *= num
    for num in range(1, n_num - r_num + 1):
        return_num //= num
    return return_num


T = int(input())
test_list = [0] * T
for i in range(T):
    test_list[i] = tuple(map(int, input().split()))

ans_list_1 = [0] * T
ans_list_2 = [0] * T

st = time.time()
for i, case in enumerate(test_list):
    n, r = case
    ans_list_1[i] = conbi(n, r)

print(time.time() - st)

st2 = time.time()
for i, case in enumerate(test_list):
    n, r = case
    ans_list_2[i] = conbi_2(n, r)

print(time.time() - st2)

print(ans_list_1 == ans_list_2)