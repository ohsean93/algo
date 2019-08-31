import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str_origin = input()
    ans = -1
    max_num = 0
    check_list = [0] * 5
    check_num = 'croak'
    for char in str_origin:
        if char == 'c':
            check_list[0] += 1

        elif char == 'r':
            check_list[1] += 1
            if check_list[0] < check_list[1]:
                break

        elif char == 'o':
            check_list[2] += 1
            if check_list[1] < check_list[2]:
                break

        elif char == 'a':
            check_list[3] += 1
            if check_list[2] < check_list[3]:
                break

        elif char == 'k':
            check_list[4] += 1
            if check_list[3] < check_list[4]:
                break
        else:
            break
        a = check_list[-1]
        b = check_list[0]

        if a:
            for i in range(5):
                check_list[i] -= a

        if max_num < b:
            max_num = b

    else:
        if not check_list[0]:
            ans = max_num

    print('#{} {}'.format(test_case, ans))