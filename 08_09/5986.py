import sys

sys.stdin = open("input.txt", "r")

p_num = [2]
for num in range(3, 32, 2):
    for div_num in range(2, num):
        if (num % div_num == 0) and (num != div_num):
            break
    else:
        p_num.append(num)

n = len(p_num)
print(p_num)
T = int(input())
for test_case in range(T):
    count = 0
    test_num = int(input())
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if test_num == p_num[i] + p_num[j] + p_num[k]:
                    count += 1
                    break

    print(test_case+1, count)