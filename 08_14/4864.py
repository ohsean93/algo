import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    taget = input()
    search = input()
    n, m, count = len(taget), len(search), 0

    for i in range(m-n+1):
        if search[i:i+n] == taget:
            count += 1

    print('#{} {}'.format(test_case+1, count))