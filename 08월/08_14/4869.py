import sys

sys.stdin = open("input.txt", "r")
T = int(input())

ans_list = [1] + [1] * 30
check_num = 1
for test_case in range(T):
    num = int(input()) // 10
    if check_num < num:
        for n in range(check_num+1, num+1):
            ans_list[n] = ans_list[n-1] + 2 * ans_list[n-2]
        check_num = num
    ans = ans_list[num]

    print('#{} {}'.format(test_case + 1, ans))