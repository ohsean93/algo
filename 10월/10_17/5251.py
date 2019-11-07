import sys

sys.stdin = open('input.txt', 'r')


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


T = int(input())
for test_case in range(1, T + 1):
    n, e = map(int, input().split())
    n += 1
    heap = [0] * (n**2)
    index = 0
    linked_list = [[] for _ in range(n+1)]
    d_matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for __ in range(e):
        s_n, e_n, w = map(int, input().split())
        d_matrix[s_n][e_n] = w
        linked_list[s_n].append(e_n)

    visit = [1] * (n + 1)
    cost = [10 ** n] * (n + 1)

    cost[0] = 0

    push_heap(heap, (0, 0))
    end_point = n - 1

    while heap:
        min_node = 0
        ans, node = pop_heap(heap)
        while visit[node] == 0:
            ans, node = pop_heap(heap)
        if node == end_point:
            break

        visit[node] = 0
        temp_cost = cost[node]
        for next_node in linked_list[node]:
            if visit[next_node]:
                c = cost[next_node] = min(cost[next_node], temp_cost + d_matrix[node][next_node])
                push_heap(heap, (c, next_node))

    print('#{} {}'.format(test_case, ans))