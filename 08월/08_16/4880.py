import sys


def rcp(a, b):
    global num_list
    v_a = num_list[a]
    v_b = num_list[b]
    checker = (v_a - v_b) % 3
    if checker == 2:
        return b
    else:
        return a


def div_con(l, r):
    if l == r:
        return l

    m = (l + r) // 2
    a = div_con(l, m)
    b = div_con(m+1, r)
    return rcp(a, b)


sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    n = int(input())
    num_list = tuple(map(int, input().split()))

    ans = div_con(0, n - 1) + 1
    print('#{} {}'.format(test_case+1, ans))