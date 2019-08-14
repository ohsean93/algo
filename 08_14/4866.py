import sys

sys.stdin = open("input.txt", "r")
T = int(input())

bracket = [('(', ')'), ('{', '}')]
bracket_o = ['(', '{']
bracket_c = [')', '}']
for test_case in range(T):
    check_list = [0]
    ans = 1
    for char in input():
        if char in bracket_c:
            a = check_list.pop(-1)
            if (a, char) in bracket:
                continue
            else:
                ans = 0
                break
        if char in bracket_o:
            check_list.append(char)
    if check_list != [0]:
        ans = 0

    print('#{} {}'.format(test_case + 1, ans))

    # 리스트 = [{, (, }]