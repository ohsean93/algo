import sys

sys.stdin = open('input.txt', 'r')


def check(can_bee_list):
    global memo, c

    p = len(can_bee_list)
    a = tuple(sorted(can_bee_list[0:p // 2]))
    b = tuple(sorted(can_bee_list[p // 2:]))

    if memo.get(a):
        temp_max = memo[a]
    else:
        temp_list = [(0, 0)]
        temp_max = 0
        for num in a:
            new_temp_list = []
            for cost, price in temp_list:
                next_cost = cost + num
                next_price = price + num**2
                if next_cost <= c:
                    new_temp_list.append((next_cost, next_price))
                    if temp_max < next_price:
                        temp_max = next_price
            temp_list += new_temp_list
            memo[a] = temp_max

    if memo.get(b):
        temp_max_2 = memo[b]
    else:
        temp_list = [(0, 0)]
        temp_max_2 = 0
        for num in can_bee_list[p//2:]:
            new_temp_list = []
            for cost, price in temp_list:
                next_cost = cost + num
                next_price = price + num ** 2
                if next_cost <= c:
                    new_temp_list.append((next_cost, next_price))
                    if temp_max_2 < next_price:
                        temp_max_2 = next_price
            temp_list += new_temp_list
        memo[b] = temp_max_2
    return temp_max + temp_max_2


T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    can_rec = set()
    visit_rec = 2**m - 1
    can_bee = set()
    memo = dict()
    max_price = 0

    for i in range(n):
        line = matrix[i]
        new_rec = set()
        if m > n // 2:
            for j in range(n-m+1):
                temp = line[j:j + m]
                for rec in can_rec:
                    check_list = tuple(list(rec) + temp)
                    new_price = check(check_list)
                    if max_price < new_price:
                        max_price = new_price
                new_rec.add(tuple(sorted(temp)))
        else:
            in_line = []
            for j in range(n - m + 1):
                temp = line[j:j + m]
                for visit, rec in in_line:
                    if visit & (visit_rec << j) == 0:
                        check_list = tuple(list(rec) + temp)
                        new_price = check(check_list)
                        if max_price < new_price:
                            max_price = new_price
                in_line.append((visit_rec << j, temp))

                for rec in can_rec:
                    check_list = tuple(list(rec) + temp)
                    new_price = check(check_list)
                    if max_price < new_price:
                        max_price = new_price
                new_rec.add(tuple(temp))
        can_rec = can_rec.union(new_rec)

    print('#{} {}'.format(test_case, max_price))
