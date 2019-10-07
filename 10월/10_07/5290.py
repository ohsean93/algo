T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    if n > 10:
        print('#{} {:.5f}'.format(test_case, 0))
        continue
    num = 1
    for i in range(10-n+1, 10):
        num *= i
    print('#{} {:.5f}'.format(test_case, num/(10**(n-1))))