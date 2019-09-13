import sys

sys.stdin = open('input.txt', 'r')

len_code = []
for r in range(1, 500//56+1):
    len_code.append(2**(r * 56))
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

num_list = {
    13: 0,
    25: 1,
    19: 2,
    61: 3,
    35: 4,
    49: 5,
    47: 6,
    59: 7,
    55: 8,
    11: 9,
}


T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    n, m = map(int, input().split())
    checker = 0
    list_code = set()
    for _ in range(n):
        temp = int('0x' + input(), 16)
        if temp != checker:
            checker, temp = temp, abs(temp - checker)
            while temp % 2 - 1:
                temp //= 2
            list_code.add(temp)

    while list_code:
        case = list_code.pop()
        checker = case
        code = []
        d = 1
        for i in range(500//56+1):
            if checker < len_code[i]:
                d = 2**(i + 1)-1
                break
        checker //= d
        while checker:
            code.append(num_list[checker % 128])
            checker //= 128
            if checker % 2 == 0 and checker != 0:
                while checker % 2 - 1:
                    checker //= 2
                list_code.add(checker)

                break
        a, b = sum(code[0::2]), sum(code[1::2])
        if (a+3*b) % 10:
            ans += 0
        else:
            ans += (a + b)
    print('#{} {}'.format(test_case, ans))