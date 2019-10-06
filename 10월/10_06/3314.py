T = int(input())
ans_list = []
for test_case in range(1, T + 1):
    sum_num = 0
    num_list = list(map(int, input().split()))
    for num in num_list:
        if num < 40:
            sum_num += 40
        else:
            sum_num += num
    ans_list.append('#{} {}'.format(test_case, sum_num//5))

print('\n'.join(ans_list))