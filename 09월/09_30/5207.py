import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    list_A = sorted(list(map(int, input().split())))
    list_B = list(map(int, input().split()))
    cnt = 0
    for num in list_B:
        checker = 0
        r = n-1
        l = 0
        m = (l + r) // 2
        while l != m and r != m:
            m = (l+r)//2
            if list_A[m] < num:
                if checker == 1:
                    break
                else:
                    checker = 1
                    l = m+1
            elif list_A[m] > num:
                if checker == 2:
                    break
                else:
                    checker = 2
                    r = m-1
            else:
                cnt += 1
                break
    print('#{} {}'.format(test_case, cnt))