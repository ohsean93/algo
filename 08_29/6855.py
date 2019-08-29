import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):

    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    if n <= k:
        ans = 0
    else:
        con_list = [0] * (n - 2)
        max_num = num_list[-1] - num_list[0]

        for i in range(n-1):
            if i == n - 2:
                continue
            else:
                con_list[i] = num_list[i + 1] - num_list[i]
        con_list.sort()
        con_list.reverse()
        ans = max_num - sum(con_list[:(k-1)])

    print('#{} {}'.format(test_case+1, ans))