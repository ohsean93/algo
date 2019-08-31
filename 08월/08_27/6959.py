import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    num = list(map(int, list(input())))
    ans = 0
    while True:
        n = len(num)
        if n == 1:
            break
        else:
            ans += 1
            tem = num[0] + num[1]
            if tem >= 10:
                num[0] = 1
                num[1] = tem - 10
            else:
                num.pop(0)
                num[0] = tem

    if ans % 2:
        ans = 'A'
    else:
        ans = 'B'
    print('#{} {}'.format(test_case+1, ans))