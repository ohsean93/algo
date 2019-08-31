import sys

sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     print('#{} {}'.format(test_case, num_list[m%n]))

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(m):
        tem = queue.pop(0)
        queue.append(tem)

    ans = queue[0]
    print('#{} {}'.format(test_case+1, ans))