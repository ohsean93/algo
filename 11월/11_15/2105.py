import sys

sys.stdin = open('input.txt', 'r')


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


def solve(l_1, l_2, m_1, m_2):
    p_1 = ((l_1 + m_1) // 2, (l_1 - m_1) // 2)
    p_2 = ((l_1 + m_2) // 2, (l_1 - m_2) // 2)
    p_4 = ((l_2 + m_1) // 2, (l_2 - m_1) // 2)
    p_3 = ((l_2 + m_2) // 2, (l_2 - m_2) // 2)
    if is_wall(*p_1) and is_wall(*p_2) and is_wall(*p_3) and is_wall(*p_4):
        global matrix
        case_boolean = [1] * 101
        point = list(p_1)
        len_path = 0
        while point[0] != p_2[0]:
            temp = matrix[point[0]][point[1]]
            if case_boolean[temp]:
                len_path += 1
                case_boolean[temp] = 0
            else:
                return
            point[0] += 1
            point[1] -= 1
        while point[0] != p_3[0]:
            temp = matrix[point[0]][point[1]]
            if case_boolean[temp]:
                len_path += 1
                case_boolean[temp] = 0
            else:
                return
            point[0] += 1
            point[1] += 1
        while point[0] != p_4[0]:
            temp = matrix[point[0]][point[1]]
            if case_boolean[temp]:
                len_path += 1
                case_boolean[temp] = 0
            else:
                return
            point[0] -= 1
            point[1] += 1
        while point[0] != p_1[0]:
            temp = matrix[point[0]][point[1]]
            if case_boolean[temp]:
                len_path += 1
                case_boolean[temp] = 0
            else:
                return
            point[0] -= 1
            point[1] -= 1
        local_max = len_path
        global ans
        if ans < local_max:
            ans = local_max


base_boolean = [1] * 101
T = int(input())
for test_case in range(1, T + 1):
    memo = dict()
    n = int(input())
    ans = -1
    matrix = [tuple(map(int, input().split())) for _ in range(n)]
    for a_1 in range(1, 2 * n - 2):
        for b_1 in range(-n, n-1):
            if (a_1 + b_1)%2:
                continue
            for a_2 in range(a_1 + 2, 2 * n - 2, 2):
                for b_2 in range(b_1 + 2, n-1, 2):
                    if (a_1 + b_1 + 1) % 2:
                        solve(a_1, a_2, b_1, b_2)

    print('#{} {}'.format(test_case, ans))
