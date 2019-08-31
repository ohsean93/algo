import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())
    k = n - k
    num = 0
    checker = 2 ** (n + 1) - 2
    for i in map(int, input().split()):
        num += 1 << i
    ans = (checker ^ num) >> 1
    num = 0
    print('#{}'.format(test_case + 1), end=' ')
    while k > 0:
        num += 1
        if ans % 2:
            print(num, end=' ')
            k -= 1
        ans >>= 1
    print()