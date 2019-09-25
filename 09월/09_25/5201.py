import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    container = sorted(list(map(int, input().split())))
    truck = sorted(list(map(int, input().split())))
    ans = 0
    while container and truck:
        a, b = container[-1], truck[-1]
        if a <= b:
            ans += a
            truck.pop()
        container.pop()

    print('#{} {}'.format(test_case, ans))