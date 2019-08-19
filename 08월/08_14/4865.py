import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    taget = input()
    search = input()
    b = dict()
    for char in search:
        if b.get(char):
            b[char] += 1
        else:
            b[char] = 1

    max_num = 0
    for char in taget:
        if max_num < b[char]:
            max_num = b[char]

    print('#{} {}'.format(test_case + 1, max_num))