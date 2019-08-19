import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    T = int(input())
    list1 = input()
    list2 = list1.split(" ")
    min_num = int(list2[0])
    max_num = int(list2[0])

    for i in range(1, T):

        if int(list2[i]) < int(min_num):
            min_num = list2[i]

        if int(list2[i]) > int(max_num):
            max_num = list2[i]
    ans = int(max_num) - int(min_num)
    print('#{0} {1}'.format(test_case, ans))