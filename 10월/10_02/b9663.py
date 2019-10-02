n = int(input())

# x, y, 합, 차 4가지 visit 이 필요, 차는 x-y+n-1로 정의
# 각 사이즈는 n, 2^n-1, 2^(2n-1)-1, 2^(2n-1)-1
visit = (0, 0, 0, 0)
cnt = 0


def n_queen(row, y_visit, add_visit, sub_visit):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        if (1 << i) & y_visit == 0 and (1 << (i+row)) & add_visit == 0 and (1 << (n-i-1+row)) & sub_visit == 0:
            n_queen(row+1, (1 << i) + y_visit, (1 << (i+row)) + add_visit, (1 << (n-i-1+row)) + sub_visit)


n_queen(*visit)
print(cnt)