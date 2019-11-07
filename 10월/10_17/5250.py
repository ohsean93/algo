import sys

sys.stdin = open('input.txt', 'r')

vector = ((0, 1), (1, 0), (0, -1), (-1, 0))


def pop_heap(origin_heap):
    global index, n
    return_element = origin_heap[1]
    origin_heap[1] = origin_heap[index]
    origin_heap[index] = 0
    index -= 1
    temp_list = [1]
    while temp_list:
        p_temp = temp_list.pop()
        if p_temp * 2 == index:
            l_temp = p_temp * 2
            if origin_heap[p_temp][0] > origin_heap[l_temp][0]:
                origin_heap[p_temp], origin_heap[l_temp] = origin_heap[l_temp], origin_heap[p_temp]
        elif p_temp * 2 < index:
            l_temp = p_temp * 2
            r_temp = p_temp * 2 + 1
            if origin_heap[p_temp][0] > origin_heap[l_temp][0]:
                origin_heap[p_temp], origin_heap[l_temp] = origin_heap[l_temp], origin_heap[p_temp]
                temp_list.append(l_temp)
            if origin_heap[p_temp][0] > origin_heap[r_temp][0]:
                origin_heap[p_temp], origin_heap[r_temp] = origin_heap[r_temp], origin_heap[p_temp]
                temp_list.append(r_temp)
    return return_element


def push_heap(origin_heap, element):
    global index
    index += 1
    origin_heap[index] = element
    temp_index = index
    p_temp = temp_index//2
    while p_temp and origin_heap[p_temp][0] >= origin_heap[temp_index][0]:
        origin_heap[p_temp], origin_heap[temp_index] = origin_heap[temp_index], origin_heap[p_temp]
        p_temp, temp_index = p_temp//2, temp_index//2
    return


def cost_move(s_p_x, s_p_y, e_p_x, e_p_y,):
    global matrix
    a, b = matrix[s_p_x][s_p_y], matrix[e_p_x][e_p_y]
    if a < b:
        return b - a + 1
    else:
        return 1


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    heap = [0] * (n**2)
    index = 0
    max_num = 10 ** 7
    matrix = [list(map(int, input().split())) for _ in range(n)]
    d_matrix = [[max_num] * n for _ in range(n)]
    visit = [[1] * n for _ in range(n)]
    d_matrix[0][0] = 0

    push_heap(heap, (0, 0, 0))
    end_point = (n-1, n-1)

    while heap:
        min_axis = (0, 0)
        x, y = add_point = pop_heap(heap)[1:]
        while visit[x][y] == 0:
            x, y = add_point = pop_heap(heap)[1:]
        if add_point == end_point:
            ans = d_matrix[n-1][n-1]
            break

        x, y = add_point
        visit[x][y] = 0
        temp_d = d_matrix[x][y]
        for dx, dy in vector:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < n and 0 <= next_y < n and visit[next_x][next_y]:
                new_cost = temp_d + cost_move(x, y, next_x, next_y)
                d = d_matrix[next_x][next_y] = min(d_matrix[next_x][next_y], new_cost)
                push_heap(heap, (d, next_x, next_y))

    print('#{} {}'.format(test_case, ans))