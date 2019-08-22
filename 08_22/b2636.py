import sys

sys.stdin = open("input.txt", "r")
#
# def bye_chi():
# #   이 함수는 녹는 치즈를 구하고 그 치즈를 보내버리는 함수(메인)
# #   0,0 에 -1을 넣는다.
# #   확산
# #   이후 1을 검사해 1이 상하좌우에 있으면 리스트에 넣는다.
# #   좌표들의 리스트를 참조하여 1=>0으로 바꾼다.
# #   반복한다.
# #   만약 1의 갯수가 0이면
# #   이전 삭제 리스트의 길이와 시행 횟수를 출력한다.
# #   공기를 -1로 두면?
# #   -1을 만나면 삭제!
#
#

udlr = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(p_x, p_y):
    global matrix

    for dal_x, dal_y in udlr:
        x, y = p_x + dal_x, p_y + dal_y
        if is_wall(x, y):
            if matrix[x][y] == 0:
                matrix[x][y] = -1
                dfs(x, y)


#     최초 범위를 넘는지 확인하는 함수
def is_wall(check_x, check_y):
    if 0 <= check_x < n and 0 <= check_y < m:
        return True
    return False


def search(p_x, p_y):
    for dal_x, dal_y in udlr:
        x, y = p_x + dal_x, p_y + dal_y
        if is_wall(x, y):
            if matrix[x][y] == -1:
                return True
    else:
        return False


ans = 0

n, m = map(int, input().split())
matrix = [0] * n
for i in range(n):
    matrix[i] = list(map(int, input().split()))

matrix[0][0] = -1
# for i in range(n):
#     print(matrix[i])

list_one = []

dfs(0, 0)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            list_one.append((i, j))

cnt = 0
while True:
    if len(list_one) == 0:
        ans = len(list_c)
        break

    cnt += 1
    list_c = []
    new_one_list = []
    for i, j in list_one:
        if search(i, j):
            list_c.append((i, j))
            matrix[i][j] = 0
        else:
            new_one_list.append((i, j))

    list_one = new_one_list
    for i, j in list_c:
        matrix[i][j] = -1
        dfs(i, j)

print(cnt)
print(ans)