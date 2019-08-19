import sys

sys.stdin = open("input.txt", "r")

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for test_case in range(T):
    t, num = input().split()
    num = int(num)
    num_str_list = input().split()
    count_list = [0] * 10

    for i in range(num):
        for index in range(10):
            if num_str_list[i] == num_list[index]:
                count_list[index] += 1

    print('#{}'.format(test_case+1))
    ans_list = []
    for i in range(10):
        ans_list += [num_list[i]]*count_list[i]

    print(' '.join(ans_list))

