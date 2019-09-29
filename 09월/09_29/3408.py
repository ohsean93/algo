ans_list = []

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ans = '#{} {} {} {}'.format(test_case, (n*(n+1)//2), n**2, n*(n+1))
    ans_list.append(ans)

print('\n'.join(ans_list))