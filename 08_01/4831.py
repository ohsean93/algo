import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = list(map(int, input().split(" ")))
    list_bus_stop = list(map(int, input().split(" ")))

    j = 0

    start = 0
    count = 0
    for i in range(len(list_bus_stop)-1):
        if list_bus_stop[i+1] - list_bus_stop[i] > k:
            count  = 0
            break
        else:
            if start+k < list_bus_stop[i+1]:
                start = list_bus_stop[i]
                count +=1

    print('#{} {}'.format(test_case, count))