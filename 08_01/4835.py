T = int(input()) + 1

for test_case in range(1, T):
    n, m = tuple(map(int, input().split()))
    main_list = list(map(int,input().split()))
    max_num = 0
    min_num = 10000 * m

    for i in range(n-m+1):
        check_list = main_list[i:i + m]
        sum_num = 0
        for num in check_list:
            sum_num += num
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num

    ans = max_num - min_num
    print('#{} {}'.format(test_case, ans))
