for test_case in range(1, 11):

    n = int(input())
    ans = 0
    list_bls = list(map(int, input().split()))

    for i in range(2, n-2):
        search_bls = [list_bls[i - 2], list_bls[i - 1], list_bls[i + 1], list_bls[i + 2]]
        max_floor = 0

        for floor in search_bls:
            if floor > max_floor:
                max_floor = floor

        bl = list_bls[i]

        if bl <= max_floor:
            continue
        else:
            ans = ans + bl - max_floor
    print('#{} {}'.format(test_case, ans))