import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    s = list(input())
    i = -1

    while True:
        i += 1
        n = len(s)
        if i < 0:
            continue
        if i >= n-1:
            break
        char1 = s[i + 1]
        char2 = s[i]

        if char1 == char2:
            s.pop(i)
            s.pop(i)
            i -= 2
    print('#{} {}'.format(test_case + 1, len(s)))