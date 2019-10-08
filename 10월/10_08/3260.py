T = int(input())
ans_list = []
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    ans_list.append('#{} {}'.format(test_case, a+b))
print('\n'.join(ans_list))