import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    cnt_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    ans = 0

    n, m, k = map(int, input().split())

    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        x_1, y_1, x_2, y_2, d = map(int, input().split())
        checker = 1
        for i in range(x_1, x_2 + 1):
            for j in range(y_1, y_2 + 1):
                if matrix[i][j] > d:
                    checker = 0
        if checker:
            for i in range(x_1, x_2 + 1):
                for j in range(y_1, y_2 + 1):
                    if matrix[i][j] < d:
                        matrix[i][j] = d

    for i in range(n):
        for j in range(m):
            cnt_dict[matrix[i][j]] += 1

    for v in cnt_dict.values():
        if ans < v:
            ans = v

    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d %d" % (test_case, ans))
