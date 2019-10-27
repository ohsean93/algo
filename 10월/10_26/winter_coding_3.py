# 최소신장 트리 => 노드는 높이 차가 HEIGHT 보다 작은 칸들의 그룹
#               => 간선은 노드별로 연결된 사다리의 코스트를 가중치로 가지는 간선
# 따라서 노드는 dfs로 구해서 묶고 각 노드간의 최소 코스트를 구한뒤 이를 이용해 최소 신장 트리를 구한다 => 최소 신장 트리를 프림 방식으로 구할 생각이기 떄문에 중복처리는 안해도 된다.
# 이때 노드 그룹도 정하지 않아도 상관없다. 어차피 프림에서 간선이 0 코스트로 확인 바로 연결된다.
from queue import PriorityQueue
n = 0
vector = ((1, 0), (0, 1), (-1, 0), (0, -1))


def is_wall(p_x, p_y):
    global n
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


def cost_edge(p_x, p_y):
    global h, matrix
    now_h = matrix[p_x][p_y]
    linked_node = []
    for dx, dy in vector:
        next_x, next_y = p_x + dx, p_y + dy
        cost = 0
        if is_wall(next_x, next_y):
            next_h = matrix[next_x][next_y]
            cost = 10000 - max(abs(next_h - now_h) - h, 0)
        linked_node.append((cost, next_x, next_y))
    return linked_node


def solution(land, height):
    global n, h, matrix
    cnt = n**2 - 1
    visit = [[1] * n for _ in range(n)]
    linked_matrix = [[] * n for _ in range(n)]
    matrix = land
    que = PriorityQueue()
    h = height
    n = len(land)
    answer = 0
    for i in range(n):
        for j in range(n):
            linked_matrix[i][j] = cost_edge(i, j)
    add_node = (0, 0)
    visit[0][0] = 0
    while cnt:
        cnt -= 1
        i, j = add_node
        for edge in linked_matrix[i][j]:
            que.put(edge)
        c, x, y = que.get()
        while visit[x][y]:
            c, x, y = que.get()
        answer += c
        add_node = (x, y)

    return answer

