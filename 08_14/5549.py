import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    num = int(input()[-1])
    if num % 2:
        print('#{} Odd'.format(test_case + 1))
    else:
        print('#{} Even'.format(test_case + 1))