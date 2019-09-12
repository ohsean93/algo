import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    happy_day_list = [0] * n
    for i in range(n):
        temp = int(input())
        happy_day_list[i] = temp
    cnt = 0

    while happy_day_list:
        new_happy_day_list = []
        temp = happy_day_list.pop(0)
        if temp == 1:
            continue
        else:
            gap = temp - 1
            for num in happy_day_list:
                if (num-1) % gap:
                    new_happy_day_list.append(num)
            cnt += 1
        happy_day_list = new_happy_day_list

    print('#{} {}'.format(test_case, cnt))
