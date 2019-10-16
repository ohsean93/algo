T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    linked_list = [set() for _ in range(n+1)]
    temp = set()
    temp.add(1)
    for __ in range(m):
        a, b = map(int, input().split())
        linked_list[a].add(b)
        linked_list[b].add(a)

    b_day = temp
    b_day = b_day.union(linked_list[1])
    for num in linked_list[1]:
        b_day = b_day.union(linked_list[num])
    ans = len(b_day)-1

    print('#{} {}'.format(test_case, ans))