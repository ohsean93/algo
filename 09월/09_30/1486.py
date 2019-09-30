import sys, time

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    st = time.time()
    temp = set()
    temp.add(0)
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    min_num = 2000000

    for height in heights:
        new_temp = set()
        for num in temp:
            sub_height = height + num
            if sub_height >= b:
                if min_num >= sub_height:
                    min_num = sub_height
                    if min_num == b:
                        break
            else:
                new_temp.add(sub_height)
        temp = temp.union(new_temp)

    print('#{} {}'.format(test_case, min_num-b))
    print(time.time()-st)