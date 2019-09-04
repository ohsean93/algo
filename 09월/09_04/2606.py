import sys

sys.stdin = open("input.txt", "r")


def bfs():
    global ans
    while queue:
        now_node = queue.pop()
        for next_node in link_list[now_node]:
            if node_list[next_node]:
                node_list[next_node] = 0
                queue.append(next_node)
                ans += 1


v = int(input())
e = int(input())
ans = 0
link_list = [[] for _ in range(v + 1)]
node_list = [1] * (v + 1)
node_list[1] = 0

a = range(e)
for _ in a:
    s_v, e_v = map(int, input().split())
    link_list[s_v].append(e_v)
    link_list[e_v].append(s_v)

queue = [1]
bfs()

print(ans)