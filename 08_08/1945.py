import sys

sys.stdin = open("input.txt", "r")

p_nums = [2, 3, 5, 7, 11]

for test_case in range(int(input())):
    count_num = [0, 0, 0, 0, 0]
    num = int(input())

    for i in range(5):
        while num % p_nums[i] == 0:
            count_num[i] += 1
            num = num // p_nums[i]


    a, b, c, d, e = tuple(count_num)
    print('#{} {} {} {} {} {}'.format(test_case+1, a, b, c, d, e))