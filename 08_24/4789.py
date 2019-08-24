import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    sum_list = []
    ans = 0

    input_list = list(map(int, list(input())))
    for i, num in enumerate(input_list):
        if i:
            sum_list.append(sum_list[i-1] + num)
            if ans < (i - sum_list[i - 1]):
                ans = i - sum_list[i - 1]
        else:
            sum_list.append(num)
    print('#{} {}'.format(test_case+1, ans))