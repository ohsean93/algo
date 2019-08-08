import sys

sys.stdin = open("input.txt", "r")


for test_case in range(int(input())):
    bus_stop = [0]*5001

    n = int(input())

    for i in range(n):
        start, end = map(int,input().split())
        for i in range(start,end+1):
            bus_stop[i] += 1

    p = int(input())
    
    print('#{}'.format(test_case+1),end=' ')
    for i in range(p):
        if i == p - 1:
            n = int(input())
            print(bus_stop[n])
        else:
            n = int(input())
            print(bus_stop[n],end=' ')