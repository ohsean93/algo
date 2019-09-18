import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    num = float(input())
    num *= (2 ** 12)
    if num - int(num):
        ans = 'overflow'
        print('#{} {}'.format(test_case, ans))
        continue
    num = bin(int(num))[2:]

    n = 12
    checker = len(num) % n
    if checker:
        num = ('0' * (n - checker)) + num
    num = list(num)
    while num.pop() == '0':
        pass
    ans = ''.join(num + ['1'])
    print('#{} {}'.format(test_case, ans))