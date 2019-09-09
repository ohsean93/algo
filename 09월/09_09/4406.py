T = int(input())
for test_case in range(1, T + 1):
    origin_str = input()

    for char in 'aeoiu':
        origin_str = origin_str.replace(char, '')

    print('#{} {}'.format(test_case, origin_str))