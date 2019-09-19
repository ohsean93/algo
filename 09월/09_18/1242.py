import sys

sys.stdin = open('input.txt', 'r')

# len_code = []
# for r in range(1, 500//56 + 2):
#     len_code.append(2**(r * 56))
# print(int('0b0001101', 2))  # 0 13
# print(int('0b0011001', 2))  # 1 25
# print(int('0b0010011', 2))  # 2 19
# print(int('0b0111101', 2))  # 3 61
# print(int('0b0100011', 2))  # 4 35
# print(int('0b0110001', 2))  # 5 49
# print(int('0b0101111', 2))  # 6 47
# print(int('0b0111011', 2))  # 7 59
# print(int('0b0110111', 2))  # 8 55
# print(int('0b0001011', 2))  # 9 11

# num_list = {
#     13: 0,
#     25: 1,
#     19: 2,
#     61: 3,
#     35: 4,
#     49: 5,
#     47: 6,
#     59: 7,
#     55: 8,
#     11: 9,
# }

num_list = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}
T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    n, m = map(int, input().split())
    code_list = set()
    temp = 0
    for _ in range(n):
        line = input()
        b = int(line, 16)

        if temp ^ b and b:
            hide_code = bin(int(line.strip('0'), 16))[2:].strip('0')
            find_code = []
            cnt = 1
            mod = '0'
            for num in hide_code:

                if num == mod:
                    cnt += 1
                else:
                    find_code.append(cnt)

                    if mod == '1':
                        mod = '0'
                        cnt = 1
                    else:
                        mod = '1'
                        cnt = 1

            find_code.append(cnt)
            temp = b

            while find_code:
                one_code = find_code[:32]
                find_code = find_code[32:]
                code = []
                d = min(list(one_code[1:]))

                while one_code:
                    checker = one_code[1:4]
                    checker = ''.join([str(x//d) for x in checker])
                    code.append(num_list[checker])
                    one_code = one_code[4:]
                code_list.add(tuple(code))

    for code in code_list:
        a, b = sum(code[1::2]), sum(code[0::2])

        if (a+3*b) % 10:
            ans += 0
        else:
            ans += (a + b)
    print('#{} {}'.format(test_case, ans))













# T = int(input())
# for test_case in range(1, T + 1):
#     ans = 0
#     n, m = map(int, input().split())
#     checker = 0
#     list_code = set()
#     temp = '0' * m
#
#     while list_code:
#         case = list_code.pop()
#         checker = case
#         ok_num = 1
#         code = []
#         d = 1
#         for i in range(500//56 + 1):
#             if checker < len_code[i]:
#                 d = i+1
#                 break
#         n = 56
#         checker = bin(checker)[2:]
#         checker_num = len(checker) % n
#         if checker_num:
#             checker = ('0' * (n - checker_num)) + checker
#
#         one = '1' * d
#         zero = '0' * d
#         checker2 = ''
#
#         while checker:
#             temp = checker[:d]
#             checker = checker[d:]
#             if temp == one:
#                 checker2 += '1'
#             elif temp == zero:
#                 checker2 += '0'
#             else:
#                 break
#         checker = checker2
#         if len(checker) != 56:
#             continue
#         checker = int(checker, 2)
#         while checker:
#             if num_list.get(checker % 128) or (checker % 128 == 13):
#                 code.append(num_list[checker % 128])
#                 checker //= 128
#             else:
#                 ok_num = 0
#                 break
#         if ok_num:
#             a, b = sum(code[0::2]), sum(code[1::2])
#             if (a+3*b) % 10:
#                 ans += 0
#             else:
#                 ans += (a + b)
#     print('#{} {}'.format(test_case, ans))