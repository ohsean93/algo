import sys

sys.stdin = open('input.txt', 'r')

num_code = {
    (1, 1, 2, 3): 0,
    (1, 2, 2, 2): 1,
    (2, 2, 1, 2): 2,
    (1, 1, 4, 1): 3,
    (2, 3, 1, 1): 4,
    (1, 3, 2, 1): 5,
    (4, 1, 1, 1): 6,
    (2, 1, 3, 1): 7,
    (3, 1, 2, 1): 8,
    (2, 1, 1, 3): 9,
}

T = int(input())
for test_case in range(1, 2):
    n, m = map(int, input().split())
    checker = [0] * m
    for _ in range(n):
        line = list(map(int, list(input())))
        for i in range(m):
            checker[m - i - 1] += line[i]

    null_str = [0] * 7

    index = 0
    while not checker[index]:
        index += 1

    code_height = checker[index]
    checker = checker[index:]

    case_code = []

    while len(checker) >= 7:
        temp_list = checker[:7]
        checker = checker[7:]
        if temp_list == null_str:
            break

        len_code = [0, 0, 0, 0]
        mode = 0
        temp = code_height
        for num in temp_list:
            if num != temp:
                mode += 1
                temp = num
            len_code[mode] += 1
        case_code = [num_code[tuple(len_code)]] + case_code
    ans = 0
    a = sum(case_code)
    if not (a + 2 * sum(case_code[0::2])) % 10:
        ans = a
    print('#{} {}'.format(test_case, ans))