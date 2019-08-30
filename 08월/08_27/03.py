import sys

sys.stdin = open('input.txt', 'r')


def bfs():
    global ans
    global queue
    while ans == -1:
        a, now_num_list = queue.pop(0)
        if a > 5:
            break
        if ans != -1:
            continue
        a += 1
        for i in range(1, n):
            next_num_list = SOM(i, now_num_list)
            queue.append((a, next_num_list))
            for check_list in ans_list:
                if check_list == next_num_list:
                    ans = a
                    break


def SOM(k, before_list):
    global mp
    key_list = before_list.copy()
    key_list.append(k)
    key = tuple(key_list)
    if mp.get(key):
        return mp[key]

    n_list = len(before_list) // 2
    if k <= n_list:
        new_list = before_list.copy()
        for i in range(k):
            for j in range(n_list-i-1, n_list+i+1, 2):
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    else:
        new_list = before_list.copy()[n_list:] + before_list.copy()[:n_list]
        for i in range(n-k-1):
            for j in range(n_list-i-1, n_list+i+1, 2):
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    mp[key] = new_list

    return new_list


T = int(input())
for test_case in range(1, T + 1):
    mp = dict()

    ans = -1
    n = int(input())
    num_list = list(map(int, input().split()))
    ans_list = (sorted(num_list), sorted(num_list)[::-1])

    queue = [(0, num_list)]
    for check_list in ans_list:
        if check_list == num_list:
            ans = 0
            break
    bfs()
    print('#{} {}'.format(test_case, ans))

