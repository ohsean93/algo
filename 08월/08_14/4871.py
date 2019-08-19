import sys

sys.stdin = open("input.txt", "r")

def find_path(path_list, list_e, len_path, check, g):
    if check == 1:
        return check
    start_v = path_list[len_path]
    deep = len_path + 1
    for i in list_e[start_v]:
        if i == g:
            check = 1
            return check
        if i in path_list:
            continue
        path_list[deep] = i
        check = find_path(path_list, list_e, deep, check, g)
    return check


T = int(input())
for test_case in range(T):
    v, e = map(int, input().split())
    list_p = [[] for i in range(v+1)]

    for p in range(e):
        s, g = map(int, input().split())
        if g in list_p[s]:
            continue
        else:
            list_p[s].append(g)

    s, g = map(int, input().split())
    path = [0] * v
    path[0] = s

    ans = find_path(path, list_p, 0, 0, g)

    print('#{} {}'.format(test_case + 1, ans))