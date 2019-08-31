def dfs(v_s):
    global v
    for next_v in linked_list[v_s]:
        if v[next_v]:
            continue
        else:
            print('-', end='')
            print(next_v, end='')
            v[next_v] = 1
            dfs(next_v)


e = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6), (3, 7), (6, 7)]
v = [0] * 8
linked_list = [[] for _ in range(8)]
for v_1, v_2 in e:
    linked_list[v_1].append(v_2)
    linked_list[v_2].append(v_1)

v[1] = 1
print(1, end='')
dfs(1)
print()