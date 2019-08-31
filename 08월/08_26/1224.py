import sys

sys.stdin = open("input.txt", "r")
out_dict = {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

in_dict = {
    '(': 0,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

T = 10
for test_case in range(T):
    n = int(input())
    stack_top = -1
    beack_ans_top = -1
    beack_ans = ['0'] * n
    stack = ['0'] * (n//2)

    origin_str = input()
    for i in range(n):
        if origin_str[i].isdigit():
            beack_ans_top += 1
            beack_ans[beack_ans_top] = origin_str[i]
        else:
            if stack_top == -1:
                stack_top += 1
                stack[stack_top] = origin_str[i]
                continue

            if ')' == origin_str[i]:
                while True:
                    if stack[stack_top] == '(':
                        stack_top -= 1
                        break
                    else:
                        beack_ans_top += 1
                        beack_ans[beack_ans_top] = stack[stack_top]
                        stack_top -= 1
                continue

            while in_dict[stack[stack_top]] >= out_dict[origin_str[i]]:
                beack_ans_top += 1
                beack_ans[beack_ans_top] = stack[stack_top]
                stack_top -= 1
            stack_top += 1
            stack[stack_top] = origin_str[i]
    while stack_top == 0:
        beack_ans_top += 1
        beack_ans[beack_ans_top] = stack[stack_top]
        stack_top -= 1

    for i in range(len(beack_ans)):
        if beack_ans[i].isdigit():
            stack_top += 1
            stack[stack_top] = int(beack_ans[i])
        else:
            if beack_ans[i] == '*':
                stack[stack_top - 1] = stack[stack_top - 1] * stack[stack_top]
                stack_top -= 1
            elif beack_ans[i] == '/':
                stack[stack_top - 1] = stack[stack_top - 1] / stack[stack_top]
                stack_top -= 1
            elif beack_ans[i] == '+':
                stack[stack_top - 1] = stack[stack_top - 1] + stack[stack_top]
                stack_top -= 1
            elif beack_ans[i] == '-':
                stack[stack_top - 1] = stack[stack_top - 1] - stack[stack_top]
                stack_top -= 1
            else:
                ans = -1
                break

    else:
        ans = stack[0]
    print('#{} {}'.format(test_case + 1, ans))
