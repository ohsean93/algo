import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    str_n = input()
    n = len(str_n) - 1
    int_n = int(str_n)
    ans = 0

    for num in range(10**(n//3), 10**(n//3 + 1)):
        if num**3 != int_n:
            if num**3 > int_n:
                ans = -1
                break
        else:
            ans = num
            break

    print('#{} {}'.format(test_case+1, ans))