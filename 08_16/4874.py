import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    num_list = [0] * 129
    operator = ('+', '-', '/', '*')
    i = -1

    for char in input().split():
        if char.isdigit():
            i += 1
            num_list[i] = int(char)
        elif char == '.':
            continue
        elif char in operator:
            if i < 1:
                ans = 'error'
                break
            if char == '+':
                num_list[i-1] += num_list[i]
                i -= 1
            elif char == '-':
                num_list[i-1] -= num_list[i]
                i -= 1
            elif char == '/':
                num_list[i-1] //= num_list[i]
                i -= 1
            elif char == '*':
                num_list[i-1] *= num_list[i]
                i -= 1
    else:
        if i == 0:
            ans = num_list[0]
        else:
            ans = 'error'

    print('#{} {}'.format(test_case+1, ans))