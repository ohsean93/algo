import sys

sys.stdin = open("input.txt", "r")

day = int(input())
time_table = [0] * day
for i in range(day):
    do_day, cost = map(int, input().split())
    time_table[i] = (do_day, cost)


def combi(sum_cost, start_day):
    global max_cost
    for d in range(start_day + 1, day):
        do_day, cost = time_table[d]
        if do_day + d - 1 < day:
            next_cost = sum_cost + cost
            next_day = do_day + d - 1
            combi(next_cost, next_day)
            if max_cost < next_cost:
                max_cost = next_cost


max_cost = 0
combi(0, -1)
print(max_cost)