import sys

sys.stdin = open("input.txt", "r")

ans = [0, 0, 0, 0, 0, 0, 0, 0]
money_kind = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(int(input())):
    money = int(input())
    for i in range(8):
        ans[i] = money // money_kind[i]
        money = money % money_kind[i]
    

    print('#{}\n{} {} {} {} {} {} {} {}'.format(test_case+1, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], ans[7]))