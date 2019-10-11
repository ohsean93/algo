import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_list = [0] * (n + 1)
    i = 1
    for num in map(int, input().split()):
        num_list[i] = num
        temp = i
        while temp != 1:
            p_node = temp//2
            if num_list[p_node] > num_list[temp]:
                num_list[p_node], num_list[temp] = num_list[temp], num_list[p_node]
                temp = p_node
                continue
            break
        i += 1
    sum_num = num_list[1]
    n //= 2
    while n != 1:
        sum_num += num_list[n]
        n //= 2
    print('#{} {}'.format(test_case, sum_num))