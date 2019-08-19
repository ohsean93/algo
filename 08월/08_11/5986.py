import sys

sys.stdin = open("input.txt", "r")

p_num = [2]
for num in range(3, 1000, 2):
    for div_num in range(3, num, 2):
        if (num % div_num == 0) and (num != div_num):
            break
    else:
        p_num.append(num)

n = len(p_num)
# print(p_num)
T = int(input())
for test_case in range(T):
    count = 0
    test_num = int(input())
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if test_num == p_num[i] + p_num[j] + p_num[k]:
                    count += 1
                    # print(p_num[i], p_num[j], p_num[k])
                    break

    print(test_case+1, count)

# n = len(p_num)
# count_num_list = [0] * 1000
# for i in range(n):
#     for j in range(i, n):
#         for k in range(j, n):
#             sum_num = p_num[i] + p_num[j] + p_num[k]
#             if sum_num < 1000:
#                 count_num_list[sum_num] += 1


# # print(p_num)
# T = int(input())
# for test_case in range(T):
#     count = 0
#     test_num = int(input())

#     print(test_case+1, count_num_list[test_num])